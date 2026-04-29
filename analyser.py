def analyze_logs(file_path):
    counts = {
        "INFO": 0,
        "ERROR": 0,
        "WARNING": 0
    }

    with open(file_path, "r") as file:
        for line in file:
            for key in counts:
                if line.startswith(key):
                    counts[key] += 1

    return counts


def generate_report(counts, output_file):
    with open(output_file, "w") as file:
        file.write("Log Summary Report\n")
        file.write("-------------------\n")
        for key, value in counts.items():
            file.write(f"{key}: {value}\n")


if __name__ == "__main__":
    log_file = "logs.txt"
    report_file = "report.txt"

    counts = analyze_logs(log_file)
    generate_report(counts, report_file)

    print("Report generated successfully!")
