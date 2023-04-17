import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from typing import List, Tuple

def get_cpu_usage() -> float:
    """Obtém o uso atual da CPU."""
    return psutil.cpu_percent()

def get_memory_usage() -> Tuple[int, float]:
    """Obtém o uso atual da memória (percentual e em bytes)."""
    memory = psutil.virtual_memory()
    return memory.percent, memory.used

def update_chart(frame: int, cpu_line: plt.Line2D, mem_line: plt.Line2D, 
                 cpu_text: plt.Text, mem_text: plt.Text) -> Tuple[plt.Line2D, plt.Line2D, plt.Text, plt.Text]:
    """Atualiza o gráfico com os valores de CPU e memória."""
    
    cpu_percent = get_cpu_usage()

  
    memory_percent, memory_used = get_memory_usage()


    cpu_line.set_data(list(range(frame)), [cpu_percent]*frame)
    mem_line.set_data(list(range(frame)), [memory_percent]*frame)

 
    cpu_text.set_text(f'CPU: {cpu_percent:.1f}%')
    mem_text.set_text(f'Memória: {memory_percent:.1f}% ({memory_used // (1024*1024)} MB)')

    return cpu_line, mem_line, cpu_text, mem_text

def animate_chart() -> None:
    """Cria e anima o gráfico de uso de CPU e memória."""
    fig, ax = plt.subplots()
    ax.set_ylim(0, 100)
    ax.set_xlim(0, 100)
    ax.set_title('Uso de CPU e Memória')
    ax.set_xlabel('Tempo')
    ax.set_ylabel('Uso (%)')
    cpu_line, = ax.plot([], [], label='CPU', color='#FF5733')
    mem_line, = ax.plot([], [], label='Memória', color='#C70039')
    ax.legend()

