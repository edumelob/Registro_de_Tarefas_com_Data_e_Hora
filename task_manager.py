from datetime import datetime
import os

class Task:
    def __init__(self, nome, status="Pendente", criado_em=None):
        self.nome = nome
        self.status = status
        # Se não for passada, a data é o momento atual
        self.criado_em = criado_em or datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return f"{self.nome} | {self.status} | Criado em: {self.criado_em}"


class TaskManager:
    def __init__(self, data_file="data/tasks.txt"):
        self.data_file = data_file
        self.tarefas = []
        self._carregar_tarefas()

    def _carregar_tarefas(self):
        """Lê as tarefas do arquivo se existir."""
        if not os.path.exists(self.data_file):
            return
        with open(self.data_file, "r", encoding="utf-8") as f:
            for line in f:
                nome, status, criado_em = line.strip().split(";")
                self.tarefas.append(Task(nome, status, criado_em))

    def _salvar_tarefas(self):
        """Salva todas as tarefas no arquivo."""
        with open(self.data_file, "w", encoding="utf-8") as f:
            for t in self.tarefas:
                f.write(f"{t.nome};{t.status};{t.criado_em}\n")

    def adicionar_tarefa(self, nome):
        """Adiciona uma nova tarefa com data e hora atuais."""
        nova = Task(nome)
        self.tarefas.append(nova)
        self._salvar_tarefas()
        print(f"✅ Tarefa '{nome}' adicionada com sucesso em {nova.criado_em}!")

    def listar_tarefas(self):
        """Lista todas as tarefas registradas."""
        if not self.tarefas:
            print("Nenhuma tarefa registrada.")
            return
        for i, t in enumerate(self.tarefas, start=1):
            print(f"{i}. {t}")

    def marcar_concluida(self, indice):
        """Marca uma tarefa como concluída."""
        try:
            tarefa = self.tarefas[indice - 1]
            tarefa.status = "Concluída"
            self._salvar_tarefas()
            print(f"✅ Tarefa '{tarefa.nome}' marcada como concluída!")
        except IndexError:
            print("❌ Número de tarefa inválido.")
