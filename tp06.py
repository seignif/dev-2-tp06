import subprocess
import argparse

def traceroute(target, progressive, output_file):
   
    command = ["tracert", target]  # Utilisation de tracert pour Windows

    try:
        with subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
            if progressive:
                # Afficher chaque ligne au fur et à mesure
                for line in proc.stdout:
                    print(line.strip())
            else:
                # Lire l'intégralité du résultat
                output = proc.stdout.read()
                if output_file:
                    # Enregistrer dans un fichier si demandé
                    with open(output_file, "w") as file:
                        file.write(output)
                else:
                    # Afficher dans la console
                    print(output.strip())
    except FileNotFoundError:
        print("Erreur : La commande 'tracert' est introuvable")
    except Exception as e:
        print(f"Erreur inattendue : {e}")

def main():
    # Configuration des arguments en ligne de commande
    parser = argparse.ArgumentParser(description="Traceroute en ligne de commande")
    parser.add_argument("target", help="l'adresse IP ou l'URL à tracer")
    parser.add_argument("-p", "--progressive", action="store_true", help="affiche progressive des résultats")
    parser.add_argument("-o", "--output-file", type=str, help="Fichier pour enregistrer le résultat")
    args = parser.parse_args()

    # Lancer la fonction de traceroute
    traceroute(args.target, args.progressive, args.output_file)

if __name__ == "__main__":
    main()
