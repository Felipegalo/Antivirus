import os
import logging

# Configuração do log
logging.basicConfig(
    filename='lista.log',
    level=logging.INFO,
    format='%(asctime)s - %(message)s'
)

# Função para varrer diretórios e localizar arquivos .exe e .bat
def scan_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            # Verifica se o arquivo tem extensão .exe ou .bat
            if file.lower().endswith(('.exe', '.bat')):
                file_path = os.path.join(root, file)
                logging.warning(f"Arquivo detectado: {file_path}")
                print(f"Arquivo detectado: {file_path}")

# Execução principal
if __name__ == "__main__":
    directory_to_scan = input("Digite o diretório para varredura: ")
    if os.path.exists(directory_to_scan):
        logging.info(f"Iniciando varredura no diretório: {directory_to_scan}")
        scan_directory(directory_to_scan)
        logging.info("Varredura concluída.")
        print("Varredura concluída. Verifique o arquivo 'lista' para detalhes.")
    else:
        print("Diretório inválido!")
