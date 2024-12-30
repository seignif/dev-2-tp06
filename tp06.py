import subprocess
import argparse
import re


def traceroute(target, progressive, output_file):
    command = ["tracert", target]  # Utilisation de 'tracert' pour Windows

    try:
        with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
            ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")  # Regex pour capturer les adresses IP

            if progressive:
                file = open(output_file, "w") if output_file else None
                try:
                    for line in proc.stdout:
                        match = ip_pattern.search(line)
                        if match:
                            ip = match.group()
                            print(ip)
                            if file:
                                file.write(ip + "\n")
                finally:
                    if file:
                        file.close()
            else:
                ips = []
                for line in proc.stdout:
                    match = ip_pattern.search(line)
                    if match:
                        ips.append(match.group())

                if output_file:
                    with open(output_file, "w") as file:
                        file.write("\n".join(ips))
                else:
                    print("\n".join(ips))

    except FileNotFoundError:
        print("Erreur : La commande 'tracert' est introuvable")
    except Exception as e:
        print(f"Erreur inattendue : {e}")


def main():
    # Configuration des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Traceroute en ligne de commande")
    parser.add_argument("target", help="l'adresse IP ou l'URL à tracer")
    parser.add_argument("-p", "--progressive", action="store_true", help="Affichage progressif des résultats")
    parser.add_argument("-o", "--output-file", type=str, help="Fichier pour enregistrer le résultat")
    args = parser.parse_args()

    # Lancer la fonction de traceroute
    traceroute(args.target, args.progressive, args.output_file)


if __name__ == "__main__":
    main()

