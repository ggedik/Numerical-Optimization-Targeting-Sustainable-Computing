import argparse
import subprocess
import sys

def run_and_monitor(command, max_iterations, output_file_path):
    # Start the subprocess with the provided command and arguments
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    current_iteration = 0
    with open(output_file_path, 'w') as output_file:
        try:
            for line in process.stdout:
                sys.stdout.write(line)
                sys.stdout.flush()
                output_file.write(line)
                current_iteration += 1
                if current_iteration > max_iterations:
                    print(f"Maximum iterations exceeded ({max_iterations}). Terminating process.")
                    process.terminate()
                    break

            process.stdout.close()
            process.wait()

        except Exception as e:
            print(f"An error occurred: {e}")
            process.terminate()

        finally:
            process.stdout.close()
            process.stderr.close()

def main():
    # Set up argparse to handle command-line arguments
    parser = argparse.ArgumentParser(description='Run a command with arguments and monitor iterations.')
    parser.add_argument('command', type=str, help='Command to execute')
    parser.add_argument('args', nargs=argparse.REMAINDER, help='Arguments for the command')
    parser.add_argument('max_iterations', type=int, help='Maximum number of iterations before stopping')
    parser.add_argument('output_file', type=str, help='Path to the output file where stdout will be written')

    args = parser.parse_args()

    # Prepare the command with its arguments
    full_command = [args.command] + args.args

    # Run the function with the parsed arguments
    run_and_monitor(full_command, args.max_iterations, args.output_file)

if __name__ == '__main__':
    main()
