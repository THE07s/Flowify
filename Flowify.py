import os
import glob
import subprocess
import cv2
import customtkinter as ctk
from tqdm import tqdm

def check_directory(directory):
	if not os.path.isdir(directory):
		print(f"🚫 Le dossier {directory} n'existe pas ou n'est pas accessible.")
		exit()


def execute_rife(input_folder, processed_folder, frames_number, slowness):
	print("⚡️Interpolation des images⚡️")
	exec_path = os.path.abspath("rife-ncnn-vulkan/rife-ncnn-vulkan")
	subprocess.run(["chmod", "+x", exec_path])
	model = input("Quel model voulez-vous utiliser ?\n\trife-anime\n\trife-UHD\n\trife-v4.6\n: ")

	if model == "rife-v4.6":
		args = [exec_path,
		        '-i', input_folder,
		        '-o', processed_folder,
		        '-n', f'N*{frames_number}',
		        '-s', slowness,
		        '-m', model]
	else:
		args = [exec_path,
		        '-i', input_folder,
		        '-o', processed_folder,
		        '-m', model]

	subprocess.run(args)
	print('🌈 Interpolation terminée 🙃!')


def create_video_from_images(images_folder, output_video_no_sound_path, fps_sortie):
	print("⚡️Création de la vidéo⚡️")
	images = [img for img in os.listdir(images_folder) if img.endswith('.png')]
	images.sort()
	frame = cv2.imread(os.path.join(images_folder, images[0]))
	height, width, layers = frame.shape

	fourcc = cv2.VideoWriter_fourcc(*'mp4v')
	video = cv2.VideoWriter(output_video_no_sound_path, fourcc, fps_sortie, (width, height))

	for image in tqdm(images, desc="📹 Création de la vidéo..."):
		video.write(cv2.imread(os.path.join(images_folder, image)))

	cv2.destroyAllWindows()
	video.release()

	print("La vidéo a été créée avec succès 👍")


def merge_audio(input_video, video_no_sound, final_output_video):
	print("⚡️Transfert de l'audio⚡️")
	extract_audio_cmd = f'ffmpeg ' \
	                    f'-i {input_video} ' \
	                    f'-vn ' \
	                    f'-codec copy audio.aac'
	merge_audio_cmd = f'ffmpeg ' \
	                  f'-i {video_no_sound} ' \
	                  f'-i audio.aac -c copy -map 0:v:0 ' \
	                  f'-map 1:a:0 {os.path.dirname(input_video)}/{final_output_video}'

	subprocess.call(extract_audio_cmd, shell=True)
	subprocess.call(merge_audio_cmd, shell=True)

	subprocess.call('rm audio.aac', shell=True)
	os.remove(video_no_sound)
	print("➡️Transfert de l'audio 🔊 terminé !")


input_dir = input("📂 Entrez le chemin du dossier contenant la vidéo ou la séquence d'images : ")
check_directory(input_dir)

temp_folder = os.path.join(input_dir, 'Temp')
os.makedirs(temp_folder, exist_ok=True)

processed_folder = os.path.join(temp_folder, 'Processed')
os.makedirs(processed_folder, exist_ok=True)

frames_number = input("🔢 Entrez le nombre par combien vous voulez multiplier le nombre de frames de la vidéo : ")
slowness = input("⏱ Entrez le facteur de multiplication de la vitesse de la vidéo : ")

image_file_pattern = "%07d.png"

video_files = glob.glob(os.path.join(input_dir, "*.mp4")) + \
              glob.glob(os.path.join(input_dir, "*.mov")) + \
              glob.glob(os.path.join(input_dir, "*.MOV"))

if len(video_files) == 0:
	image_files = glob.glob(os.path.join(input_dir, "*.png")) + glob.glob(os.path.join(input_dir, "*.jpg"))
	if len(image_files) == 0:
		print(f"🚫 Aucun fichier vidéo ou image trouvé dans le dossier {input_dir}")
	else:
		print(f"🖼️ Le dossier {input_dir} contient déjà une séquence d'images.")

		fps_sortie = int(input("⏩ Entrez le nombre de frames par seconde : "))
		output_video = input("🎞 Entrez un nom pour la vidéo de sortie") + f"_interpolated_to_{fps_sortie}fps.mov"

		execute_rife(input_dir, processed_folder, frames_number, slowness)

		final_output_no_sound = os.path.join(input_dir, output_video)
		create_video_from_images(processed_folder, final_output_no_sound, fps_sortie)
else:
	for video_file in tqdm(video_files, desc="🔄 Traitement des fichiers vidéo..."):
		video_path = os.path.abspath(video_file)
		video_name = os.path.splitext(os.path.basename(video_file))[0]
		image_folder = os.path.join(temp_folder, video_name)
		os.makedirs(image_folder, exist_ok=True)

		fps_entree_ffprobe = ["ffprobe",
		                      "-v", "error",
		                      "-select_streams", "v:0",
		                      "-show_entries", "stream=r_frame_rate",
		                      "-of", "default=noprint_wrappers=1:nokey=1", video_path]
		output = subprocess.check_output(fps_entree_ffprobe)
		fps_entree = eval(output.decode("utf-8").strip())

		print(f"🌟 Le nombre d'images par seconde est : {fps_entree}")

		fps_sortie = float(frames_number) * fps_entree

		final_output_video = video_name + f"_{fps_entree}fps_to_{fps_sortie}fps.mov"

		ffmpeg_extract = ["ffmpeg",
		                  "-i", video_path,
		                  "-r", str(fps_entree), os.path.join(image_folder, image_file_pattern)]
		subprocess.run(ffmpeg_extract)

		execute_rife(image_folder, processed_folder, frames_number, slowness)

		create_video_from_images(processed_folder, video_path + f"/🔇{video_name}", fps_sortie)

		merge_audio(video_path, video_path + f"/🔇{video_name}", final_output_video)


subprocess.run(["rm", "-rf", temp_folder])


