from tabulate import tabulate

# Class untuk menangani data
class TaskData:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_tasks(self):   
        return self.tasks

# Class untuk menangani tampilan (view)
class TaskView:
    @staticmethod
    def display_tasks(tasks):
        if not tasks:
            print("\nTidak ada tugas yang tersedia.")
        else:
            table = [[i + 1, task] for i, task in enumerate(tasks)]
            print("\nDaftar Tugas:")
            print(tabulate(table, headers=["No", "Tugas"], tablefmt="grid"))

    @staticmethod
    def show_message(message):
        print(f"\n{message}")

# Class untuk menangani proses bisnis
class TaskProcess:
    def __init__(self, data, view):
        self.data = data
        self.view = view

    def add_task(self):
        while True:
            try:
                task = input("Masukkan tugas baru: ").strip()
                if not task:
                    raise ValueError("Tugas tidak boleh kosong!")
                self.data.add_task(task)
                self.view.show_message("Tugas berhasil ditambahkan.")
                break
            except ValueError as e:
                self.view.show_message(f"Input tidak valid: {e}")

    def display_tasks(self):
        tasks = self.data.get_tasks()
        self.view.display_tasks(tasks)

# Main Program
def main():
    data = TaskData()
    view = TaskView()
    process = TaskProcess(data, view)

    while True:
        print("\nMenu:")
        print("1. Tambah Tugas")
        print("2. Tampilkan Tugas")
        print("3. Keluar")

        try:
            choice = int(input("Pilih menu: "))
            if choice == 1:
                process.add_task()
            elif choice == 2:
                process.display_tasks()
            elif choice == 3:
                view.show_message("Terima kasih telah menggunakan aplikasi ini.")
                break
            else:
                view.show_message("Pilihan tidak valid. Masukkan angka 1-3.")
        except ValueError:
            view.show_message("Input tidak valid. Masukkan angka.")

if __name__ == "__main__":
    main()
