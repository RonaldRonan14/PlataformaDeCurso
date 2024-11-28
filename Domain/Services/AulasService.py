from Domain.Entities.Aula import Aula
from Infrastructure.Repositories.AulaRepository import get_aulas_by_curso_id, add_aula, get_aula_by_aula_id
from moviepy.editor import VideoFileClip
import os

UPLOAD_FOLDER = 'Presentation/wwwroot/Uploads/Videos'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_aulas_by_curso_id_service(curso_id: int) -> list[Aula]:
    return get_aulas_by_curso_id(curso_id)

def get_aula_by_aula_id_service(aula_id: int) -> Aula:
    return get_aula_by_aula_id(aula_id)

def add_aula_service(curso_id: int, nome: str, descricao: str, complemento: str, video):

    if not curso_id or not nome:
        raise ValueError("O Id do curso e o nome são obrigatórios.")
    
    video_path_db = ''
    duracao_video = 0

    if (video.filename != ''):
        video_filename = f"{nome}_{video.filename}"
        video_path = f"{UPLOAD_FOLDER}/{video_filename}"
        video.save(video_path)
        video_path_db = f"Uploads/Videos/{video_filename}"

        clip = VideoFileClip(video_path)
        duracao_video = int(clip.duration)/60  # Duração em segundos
        clip.close()

    nova_aula = Aula(
        CursoId = curso_id,
        Nome = nome,
        Descricao = descricao,
        Complemento = complemento,
        Duracao = duracao_video,
        VideoPath = video_path_db
    )

    add_aula(nova_aula)