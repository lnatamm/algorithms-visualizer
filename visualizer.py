import pygame
import numpy as np
import random
import sys

# Inicializar Pygame
pygame.init()
pygame.mixer.init()

# Configurações
WIDTH = 1200
HEIGHT = 700
FPS = float('inf')

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 100, 255)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)
DARK_GRAY = (40, 40, 40)
LIGHT_GRAY = (200, 200, 200)
HOVER_BLUE = (0, 150, 255)
DARK_BLUE = (0, 50, 150)

class Button:
    def __init__(self, x, y, width, height, text, color=BLUE, hover_color=HOVER_BLUE, text_color=WHITE):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.is_hovered = False
    
    def draw(self, screen):
        color = self.hover_color if self.is_hovered else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        pygame.draw.rect(screen, WHITE, self.rect, 3, border_radius=10)
        
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
    
    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

class InputBox:
    def __init__(self, x, y, width, height, default_text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = default_text
        self.active = False
        self.color = LIGHT_GRAY
        self.active_color = WHITE
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.active = self.rect.collidepoint(event.pos)
        
        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                return True
            elif event.unicode.isdigit() and len(self.text) < 6:
                self.text += event.unicode
        return False
    
    def draw(self, screen):
        color = self.active_color if self.active else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=5)
        pygame.draw.rect(screen, BLUE, self.rect, 3, border_radius=5)
        
        font = pygame.font.Font(None, 48)
        text_surface = font.render(self.text, True, BLACK)
        screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))
    
    def get_value(self):
        try:
            return int(self.text) if self.text else 0
        except:
            return 0

class SortingVisualizer:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Sorting Algorithm Visualizer")
        self.clock = pygame.time.Clock()
        
        # Estados do menu
        self.state = 'MENU'  # MENU, CHOOSE_TYPE, SIZE_INPUT/GRAPH_CATEGORY, ALGORITHM_SELECT, SORTING, SEARCHING, GRAPH
        
        # Variáveis de configuração
        self.algorithm_type = 'sorting'  # 'sorting', 'searching' ou 'graph'
        self.graph_category = 'global'  # 'global' ou 'local'
        self.array_size = 100
        self.array = []
        self.bar_width = 0
        self.comparing = []
        self.swapping = []
        self.sorted_indices = []
        self.found_index = -1
        self.search_target = 0
        self.running = True
        
        # Variáveis de grafos
        self.graph_nodes = []
        self.graph_edges = []
        self.node_count = 10
        self.start_node = 0
        self.end_node = 0
        self.visited_nodes = []
        self.current_node = -1
        self.distances = {}
        self.path = []
        self.sound_enabled = True
        self.operation_count = 0
        self.skip_frames = 1
        
        self.sorting_algorithms = {
            'QuickSort': self.quicksort_visual,
            'Merge Sort': self.mergesort_visual,
            'Heap Sort': self.heapsort_visual,
            'Bubble Sort': self.bubblesort_visual,
            'Insertion Sort': self.insertionsort_visual,
            'Selection Sort': self.selectionsort_visual,
            'Bogo Sort': self.bogosort_visual,
        }
        
        self.search_algorithms = {
            'Busca Linear': self.linear_search_visual,
            'Busca Binária': self.binary_search_visual,
            'Busca por Interpolação': self.interpolation_search_visual,
            'Busca em Saltos': self.jump_search_visual,
            'Busca Exponencial': self.exponential_search_visual,
        }
        
        self.graph_global_algorithms = {
            'Dijkstra': self.dijkstra_visual,
            'Bellman-Ford': self.bellman_ford_visual,
            'Floyd-Warshall': self.floyd_warshall_visual,
        }
        
        self.graph_local_algorithms = {
            'BFS (Busca em Largura)': self.bfs_visual,
            'DFS (Busca em Profundidade)': self.dfs_visual,
            'A* (A-Star)': self.astar_visual,
        }
        
        self.current_algorithm = 'QuickSort'
        
        # Componentes do menu
        self.init_menu_components()
    
    def init_menu_components(self):
        """Inicializa botões e elementos do menu"""
        # Menu principal
        self.start_button = Button(WIDTH//2 - 150, HEIGHT//2 - 50, 300, 80, "INICIAR", BLUE, HOVER_BLUE)
        self.quit_button = Button(WIDTH//2 - 150, HEIGHT//2 + 60, 300, 60, "Sair", RED, (255, 100, 100))
        
        # Escolha de tipo
        self.sorting_type_button = Button(WIDTH//2 - 360, HEIGHT//2 - 50, 200, 80, "Ordenação", BLUE, HOVER_BLUE)
        self.searching_type_button = Button(WIDTH//2 - 100, HEIGHT//2 - 50, 200, 80, "Busca", GREEN, (0, 200, 100))
        self.graph_type_button = Button(WIDTH//2 + 160, HEIGHT//2 - 50, 200, 80, "Grafos", PURPLE, (180, 0, 180))
        self.type_back_button = Button(WIDTH//2 - 150, HEIGHT//2 + 80, 300, 60, "Voltar", LIGHT_GRAY, (220, 220, 220), BLACK)
        
        # Escolha de categoria de grafo
        self.global_graph_button = Button(WIDTH//2 - 250, HEIGHT//2 - 50, 220, 80, "Global", BLUE, HOVER_BLUE)
        self.local_graph_button = Button(WIDTH//2 + 30, HEIGHT//2 - 50, 220, 80, "Local", GREEN, (0, 200, 100))
        self.graph_cat_back_button = Button(WIDTH//2 - 150, HEIGHT//2 + 80, 300, 60, "Voltar", LIGHT_GRAY, (220, 220, 220), BLACK)
        
        # Input de tamanho
        self.input_box = InputBox(WIDTH//2 - 150, HEIGHT//2 - 40, 300, 80, '100')
        self.confirm_size_button = Button(WIDTH//2 - 150, HEIGHT//2 + 80, 300, 60, "Confirmar", GREEN, (0, 255, 100))
        self.back_button = Button(WIDTH//2 - 150, HEIGHT//2 + 160, 300, 50, "Voltar", LIGHT_GRAY, (220, 220, 220), BLACK)
        
        # Seleção de algoritmo (será recriado dinamicamente)
        self.algo_buttons = []
        
        # Botão voltar para seleção de algoritmo
        self.algo_back_button = Button(WIDTH//2 - 150, HEIGHT - 70, 300, 50, "Voltar", LIGHT_GRAY, (220, 220, 220), BLACK)
    
    def create_algorithm_buttons(self):
        """Cria botões de algoritmo baseado no tipo selecionado"""
        self.algo_buttons = []
        
        if self.algorithm_type == 'sorting':
            algorithms = self.sorting_algorithms
            color = PURPLE
            hover_color = (180, 0, 180)
        elif self.algorithm_type == 'searching':
            algorithms = self.search_algorithms
            color = (0, 150, 150)
            hover_color = (0, 200, 200)
        else:  # graph
            algorithms = self.graph_global_algorithms if self.graph_category == 'global' else self.graph_local_algorithms
            color = (255, 140, 0)  # Laranja
            hover_color = (255, 165, 0)
        
        algo_names = list(algorithms.keys())
        start_y = 150
        
        for i, name in enumerate(algo_names):
            button = Button(WIDTH//2 - 200, start_y + i * 68, 400, 58, name, color, hover_color)
            self.algo_buttons.append((name, button))
    
    def draw_menu(self):
        """Desenha o menu principal"""
        self.screen.fill(DARK_GRAY)
        
        # Título
        font_large = pygame.font.Font(None, 80)
        title = font_large.render("Visualizador de Ordenação", True, YELLOW)
        self.screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
        
        font_medium = pygame.font.Font(None, 40)
        subtitle = font_medium.render("Aprenda algoritmos de forma visual!", True, WHITE)
        self.screen.blit(subtitle, (WIDTH//2 - subtitle.get_width()//2, 180))
        
        # Botões
        self.start_button.draw(self.screen)
        self.quit_button.draw(self.screen)
        
        # Rodapé
        font_small = pygame.font.Font(None, 24)
        footer = font_small.render("Use o mouse para interagir", True, LIGHT_GRAY)
        self.screen.blit(footer, (WIDTH//2 - footer.get_width()//2, HEIGHT - 40))
        
        pygame.display.flip()
    
    def draw_choose_type(self):
        """Desenha a tela de escolha entre ordenação, busca e grafos"""
        self.screen.fill(DARK_GRAY)
        
        # Título
        font_large = pygame.font.Font(None, 70)
        title = font_large.render("Escolha o Tipo de Algoritmo", True, YELLOW)
        self.screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
        
        font_medium = pygame.font.Font(None, 32)
        subtitle = font_medium.render("Clique para selecionar", True, WHITE)
        self.screen.blit(subtitle, (WIDTH//2 - subtitle.get_width()//2, 180))
        
        # Botões
        self.sorting_type_button.draw(self.screen)
        self.searching_type_button.draw(self.screen)
        self.graph_type_button.draw(self.screen)
        self.type_back_button.draw(self.screen)
        
        pygame.display.flip()
    
    def draw_graph_category(self):
        """Desenha a tela de escolha de categoria de grafo"""
        self.screen.fill(DARK_GRAY)
        
        # Título
        font_large = pygame.font.Font(None, 70)
        title = font_large.render("Categoria de Busca em Grafos", True, YELLOW)
        self.screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
        
        font_medium = pygame.font.Font(None, 28)
        subtitle1 = font_medium.render("Global: Calcula distâncias de todos os nós", True, WHITE)
        subtitle2 = font_medium.render("Local: Encontra caminho entre dois nós", True, WHITE)
        self.screen.blit(subtitle1, (WIDTH//2 - subtitle1.get_width()//2, 180))
        self.screen.blit(subtitle2, (WIDTH//2 - subtitle2.get_width()//2, 215))
        
        # Botões
        self.global_graph_button.draw(self.screen)
        self.local_graph_button.draw(self.screen)
        self.graph_cat_back_button.draw(self.screen)
        
        pygame.display.flip()
    
    def draw_size_input(self):
        """Desenha a tela de input de tamanho"""
        self.screen.fill(DARK_GRAY)
        
        # Título
        font_large = pygame.font.Font(None, 60)
        title = font_large.render("Tamanho do Array", True, YELLOW)
        self.screen.blit(title, (WIDTH//2 - title.get_width()//2, 120))
        
        font_medium = pygame.font.Font(None, 36)
        instruction = font_medium.render("Digite um número entre 1 e 10000", True, WHITE)
        self.screen.blit(instruction, (WIDTH//2 - instruction.get_width()//2, 200))
        
        # Input box
        self.input_box.draw(self.screen)
        
        # Botões
        self.confirm_size_button.draw(self.screen)
        self.back_button.draw(self.screen)
        
        pygame.display.flip()
    
    def draw_algorithm_select(self):
        """Desenha a tela de seleção de algoritmo"""
        self.screen.fill(DARK_GRAY)
        
        # Título
        font_large = pygame.font.Font(None, 60)
        type_name = "Ordenação" if self.algorithm_type == 'sorting' else "Busca"
        title = font_large.render(f"Escolha o Algoritmo de {type_name}", True, YELLOW)
        self.screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))
        
        font_medium = pygame.font.Font(None, 30)
        info = font_medium.render(f"Array com {self.array_size} elementos", True, WHITE)
        self.screen.blit(info, (WIDTH//2 - info.get_width()//2, 110))
        
        # Botões de algoritmos
        for name, button in self.algo_buttons:
            button.draw(self.screen)
        
        # Botão voltar
        self.algo_back_button.draw(self.screen)
        
        pygame.display.flip()
    
    def draw(self):
        """Desenha o array como barras verticais"""
        self.screen.fill(BLACK)
        
        for i, value in enumerate(self.array):
            x = i * self.bar_width
            # Ajusta altura para ocupar mais espaço vertical
            max_height = HEIGHT - 90  # Mais espaço para as barras
            max_value = max(self.array) if self.array else 1  # Valor máximo no array
            bar_height = (value / max_value) * max_height
            y = HEIGHT - bar_height - 10  # Barras mais próximas da base
            
            # Determina a cor da barra
            if i == self.found_index:
                color = (255, 215, 0)  # Dourado para elemento encontrado
            elif i in self.sorted_indices:
                color = GREEN
            elif i in self.swapping:
                color = RED
            elif i in self.comparing:
                color = YELLOW
            else:
                color = BLUE
            
            # Garante que a barra tenha pelo menos 1 pixel de largura
            rect_width = max(1, self.bar_width - 1) if self.bar_width > 1 else 1
            pygame.draw.rect(self.screen, color, (x, y, rect_width, bar_height))
        
        # Texto de instrução
        font = pygame.font.Font(None, 28)
        if self.algorithm_type == 'searching':
            title_text = font.render(f"SPACE: Pausar | R: Reset | ESC: Menu | Alvo: {self.search_target}", True, WHITE)
        else:
            title_text = font.render("SPACE: Pausar/Continuar | R: Reset | ESC: Menu", True, WHITE)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 5))
        
        # Mostrar algoritmo atual
        font_medium = pygame.font.Font(None, 26)
        algo_text = font_medium.render(f"Algoritmo: {self.current_algorithm}", True, YELLOW)
        self.screen.blit(algo_text, (WIDTH // 2 - algo_text.get_width() // 2, 32))
        
        font_small = pygame.font.Font(None, 22)
        status = f"Operations: {self.operation_count} | Array Size: {self.array_size}"
        if self.sound_enabled:
            status += " | Sound: ON"
        else:
            status += " | Sound: OFF"
        
        status_text = font_small.render(status, True, WHITE)
        self.screen.blit(status_text, (10, HEIGHT - 25))
        
        pygame.display.flip()
        
    def play_sound(self, frequency):
        """Gera um som baseado na frequência (valor do elemento)"""
        if not self.sound_enabled:
            return
            
        # Mapeia o valor do array para uma frequência audível (200-2000 Hz)
        max_value = max(self.array) if self.array else 1
        freq = int(200 + (frequency / max_value) * 1800)
        
        # Gera uma onda sonora curta
        sample_rate = 22050
        duration = 0.02  # 20ms (mais rápido)
        n_samples = int(sample_rate * duration)
        
        # Cria uma onda senoidal
        t = np.linspace(0, duration, n_samples, False)
        wave = np.sin(2 * np.pi * freq * t)
        
        # Aplica envelope para evitar clicks
        envelope = np.linspace(1, 0, n_samples)
        wave = wave * envelope
        
        # Converte para formato de áudio do pygame
        sound_array = np.array([wave, wave]).T.copy(order='C')
        sound_array = (sound_array * 32767).astype(np.int16)
        sound = pygame.sndarray.make_sound(sound_array)
        sound.play()
    
    def quicksort_visual(self, low=0, high=None):
        """QuickSort com visualização"""
        if high is None:
            high = len(self.array) - 1
            
        if low < high:
            pi = yield from self.partition_visual(low, high)
            if self.running:
                yield from self.quicksort_visual(low, pi - 1)
            if self.running:
                yield from self.quicksort_visual(pi + 1, high)
            
    def partition_visual(self, low, high):
        """Partição do QuickSort com visualização"""
        pivot = self.array[high]
        i = low - 1
        
        for j in range(low, high):
            # Verifica eventos do pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return i + 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return i + 1
            
            if not self.running:
                return i + 1
            
            self.operation_count += 1
            
            # Visualiza a comparação
            self.comparing = [j, high]
            
            # Pula frames para arrays grandes
            if self.operation_count % self.skip_frames == 0:
                self.play_sound(self.array[j])
                self.draw()
                self.clock.tick(FPS)
            
            if self.array[j] <= pivot:
                i += 1
                # Visualiza a troca
                self.swapping = [i, j]
                self.array[i], self.array[j] = self.array[j], self.array[i]
                
                if self.operation_count % self.skip_frames == 0:
                    self.play_sound(self.array[i])
                    self.draw()
                    self.clock.tick(FPS)
                self.swapping = []
            
            yield
        
        # Troca final com o pivô
        self.swapping = [i + 1, high]
        self.array[i + 1], self.array[high] = self.array[high], self.array[i + 1]
        
        if self.operation_count % self.skip_frames == 0:
            self.play_sound(self.array[i + 1])
            self.draw()
            self.clock.tick(FPS)
        
        self.swapping = []
        self.comparing = []
        
        yield
        return i + 1
    
    def mergesort_visual(self, left=0, right=None):
        """Merge Sort com visualização"""
        if right is None:
            right = len(self.array) - 1
        
        if left < right:
            mid = (left + right) // 2
            yield from self.mergesort_visual(left, mid)
            if self.running:
                yield from self.mergesort_visual(mid + 1, right)
            if self.running:
                yield from self.merge_visual(left, mid, right)
    
    def merge_visual(self, left, mid, right):
        """Merge com visualização"""
        left_array = self.array[left:mid+1]
        right_array = self.array[mid+1:right+1]
        
        i = j = 0
        k = left
        
        while i < len(left_array) and j < len(right_array):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            self.operation_count += 1
            self.comparing = [k]
            
            if left_array[i] <= right_array[j]:
                self.array[k] = left_array[i]
                i += 1
            else:
                self.array[k] = right_array[j]
                j += 1
            
            if self.operation_count % self.skip_frames == 0:
                self.play_sound(self.array[k])
                self.draw()
                self.clock.tick(FPS)
            
            k += 1
            yield
        
        while i < len(left_array):
            self.array[k] = left_array[i]
            if self.operation_count % self.skip_frames == 0:
                self.play_sound(self.array[k])
                self.draw()
                self.clock.tick(FPS)
            i += 1
            k += 1
            yield
        
        while j < len(right_array):
            self.array[k] = right_array[j]
            if self.operation_count % self.skip_frames == 0:
                self.play_sound(self.array[k])
                self.draw()
                self.clock.tick(FPS)
            j += 1
            k += 1
            yield
        
        self.comparing = []
    
    def heapsort_visual(self):
        """Heap Sort com visualização"""
        n = len(self.array)
        
        # Constrói o heap máximo
        for i in range(n // 2 - 1, -1, -1):
            yield from self.heapify_visual(n, i)
            if not self.running:
                return
        
        # Extrai elementos do heap um por um
        for i in range(n - 1, 0, -1):
            self.swapping = [0, i]
            self.array[0], self.array[i] = self.array[i], self.array[0]
            
            if self.operation_count % self.skip_frames == 0:
                self.play_sound(self.array[0])
                self.draw()
                self.clock.tick(FPS)
            
            self.swapping = []
            self.sorted_indices.append(i)
            
            yield from self.heapify_visual(i, 0)
            if not self.running:
                return
            yield
    
    def heapify_visual(self, n, i):
        """Heapify com visualização"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    return
        
        if not self.running:
            return
        
        self.operation_count += 1
        self.comparing = [i, left, right] if right < n else ([i, left] if left < n else [i])
        
        if left < n and self.array[left] > self.array[largest]:
            largest = left
        
        if right < n and self.array[right] > self.array[largest]:
            largest = right
        
        if largest != i:
            self.swapping = [i, largest]
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            
            if self.operation_count % self.skip_frames == 0:
                self.play_sound(self.array[i])
                self.draw()
                self.clock.tick(FPS)
            
            self.swapping = []
            yield from self.heapify_visual(n, largest)
        
        self.comparing = []
        yield
    
    def bubblesort_visual(self):
        """Bubble Sort com visualização"""
        n = len(self.array)
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                            return
                
                if not self.running:
                    return
                
                self.operation_count += 1
                self.comparing = [j, j + 1]
                
                if self.operation_count % self.skip_frames == 0:
                    self.play_sound(self.array[j])
                    self.draw()
                    self.clock.tick(FPS)
                
                if self.array[j] > self.array[j + 1]:
                    self.swapping = [j, j + 1]
                    self.array[j], self.array[j + 1] = self.array[j + 1], self.array[j]
                    
                    if self.operation_count % self.skip_frames == 0:
                        self.play_sound(self.array[j])
                        self.draw()
                        self.clock.tick(FPS)
                    
                    self.swapping = []
                    swapped = True
                
                yield
            
            self.sorted_indices.append(n - i - 1)
            
            if not swapped:
                break
        
        self.comparing = []
    
    def insertionsort_visual(self):
        """Insertion Sort com visualização"""
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i - 1
            
            while j >= 0:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                            return
                
                if not self.running:
                    return
                
                self.operation_count += 1
                self.comparing = [j, j + 1]
                
                if self.operation_count % self.skip_frames == 0:
                    self.play_sound(self.array[j])
                    self.draw()
                    self.clock.tick(FPS)
                
                if self.array[j] > key:
                    self.array[j + 1] = self.array[j]
                    
                    if self.operation_count % self.skip_frames == 0:
                        self.draw()
                        self.clock.tick(FPS)
                    
                    j -= 1
                else:
                    break
                
                yield
            
            self.array[j + 1] = key
            
            if self.operation_count % self.skip_frames == 0:
                self.play_sound(self.array[j + 1])
                self.draw()
                self.clock.tick(FPS)
            
            yield
        
        self.comparing = []
    
    def selectionsort_visual(self):
        """Selection Sort com visualização"""
        n = len(self.array)
        
        for i in range(n):
            min_idx = i
            
            for j in range(i + 1, n):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                            return
                
                if not self.running:
                    return
                
                self.operation_count += 1
                self.comparing = [min_idx, j]
                
                if self.operation_count % self.skip_frames == 0:
                    self.play_sound(self.array[j])
                    self.draw()
                    self.clock.tick(FPS)
                
                if self.array[j] < self.array[min_idx]:
                    min_idx = j
                
                yield
            
            self.swapping = [i, min_idx]
            self.array[i], self.array[min_idx] = self.array[min_idx], self.array[i]
            
            if self.operation_count % self.skip_frames == 0:
                self.play_sound(self.array[i])
                self.draw()
                self.clock.tick(FPS)
            
            self.swapping = []
            self.sorted_indices.append(i)
            yield
        
        self.comparing = []
    
    def bogosort_visual(self):
        """Bogo Sort com visualização - MUITO INEFICIENTE!"""
        iterations = 0
        max_iterations = 100000  # Limite de segurança
        
        while iterations < max_iterations:
            # Verifica se está ordenado
            is_sorted = True
            for i in range(len(self.array) - 1):
                if self.array[i] > self.array[i + 1]:
                    is_sorted = False
                    break
            
            if is_sorted:
                break
            
            # Embaralha o array
            random.shuffle(self.array)
            iterations += 1
            self.operation_count += 1
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            if self.operation_count % max(1, self.skip_frames // 10) == 0:
                self.play_sound(self.array[0])
                self.draw()
                self.clock.tick(FPS * 10)  # Mais rápido para Bogo Sort
            
            yield
    
    def linear_search_visual(self):
        """Busca Linear com visualização"""
        for i in range(len(self.array)):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            self.operation_count += 1
            self.comparing = [i]
            
            # Busca é mais lenta para visualização
            self.play_sound(self.array[i])
            self.draw()
            self.clock.tick(30)  # Mais lento que ordenação
            
            if self.array[i] == self.search_target:
                self.found_index = i
                self.comparing = []
                return
            
            yield
        
        self.comparing = []
    
    def binary_search_visual(self):
        """Busca Binária com visualização (requer array ordenado)"""
        left = 0
        right = len(self.array) - 1
        
        while left <= right:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            mid = (left + right) // 2
            self.operation_count += 1
            self.comparing = [mid]
            
            # Busca é mais lenta para visualização
            self.play_sound(self.array[mid])
            self.draw()
            self.clock.tick(10)  # Bem lento para ver a busca binária
            
            if self.array[mid] == self.search_target:
                self.found_index = mid
                self.comparing = []
                return
            elif self.array[mid] < self.search_target:
                left = mid + 1
            else:
                right = mid - 1
            
            yield
        
        self.comparing = []
    
    def interpolation_search_visual(self):
        """Busca por Interpolação com visualização"""
        left = 0
        right = len(self.array) - 1
        
        while left <= right and self.search_target >= self.array[left] and self.search_target <= self.array[right]:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            if self.array[right] == self.array[left]:
                pos = left
            else:
                pos = left + int(((self.search_target - self.array[left]) / 
                                 (self.array[right] - self.array[left])) * (right - left))
            
            pos = max(left, min(pos, right))
            
            self.operation_count += 1
            self.comparing = [pos]
            
            # Busca é mais lenta para visualização
            self.play_sound(self.array[pos])
            self.draw()
            self.clock.tick(10)
            
            if self.array[pos] == self.search_target:
                self.found_index = pos
                self.comparing = []
                return
            elif self.array[pos] < self.search_target:
                left = pos + 1
            else:
                right = pos - 1
            
            yield
        
        self.comparing = []
    
    def jump_search_visual(self):
        """Busca em Saltos com visualização"""
        n = len(self.array)
        step = int(n ** 0.5)
        prev = 0
        
        while prev < n and self.array[min(step, n) - 1] < self.search_target:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            self.operation_count += 1
            self.comparing = [min(step, n) - 1]
            
            # Busca é mais lenta para visualização
            self.play_sound(self.array[min(step, n) - 1])
            self.draw()
            self.clock.tick(15)
            
            prev = step
            step += int(n ** 0.5)
            
            if prev >= n:
                break
            
            yield
        
        # Busca linear no bloco
        while prev < n:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            self.operation_count += 1
            self.comparing = [prev]
            
            # Busca é mais lenta para visualização
            self.play_sound(self.array[prev])
            self.draw()
            self.clock.tick(20)
            
            if self.array[prev] == self.search_target:
                self.found_index = prev
                self.comparing = []
                return
            
            prev += 1
            
            if prev == min(step, n):
                break
            
            yield
        
        self.comparing = []
    
    def exponential_search_visual(self):
        """Busca Exponencial com visualização"""
        if self.array[0] == self.search_target:
            self.found_index = 0
            return
        
        i = 1
        while i < len(self.array) and self.array[i] <= self.search_target:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            self.operation_count += 1
            self.comparing = [i]
            
            # Busca é mais lenta para visualização
            self.play_sound(self.array[i])
            self.draw()
            self.clock.tick(15)
            
            i = i * 2
            yield
        
        # Busca binária no intervalo
        left = i // 2
        right = min(i, len(self.array) - 1)
        
        while left <= right:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            mid = (left + right) // 2
            self.operation_count += 1
            self.comparing = [mid]
            
            # Busca é mais lenta para visualização
            self.play_sound(self.array[mid])
            self.draw()
            self.clock.tick(12)
            
            if self.array[mid] == self.search_target:
                self.found_index = mid
                self.comparing = []
                return
            elif self.array[mid] < self.search_target:
                left = mid + 1
            else:
                right = mid - 1
            
            yield
        
        self.comparing = []
    
    def setup_graph(self):
        """Configura o grafo com nós e arestas aleatórios"""
        import math
        
        self.graph_nodes = []
        self.graph_edges = []
        self.visited_nodes = []
        self.current_node = -1
        self.distances = {i: float('inf') for i in range(self.node_count)}
        self.path = []
        
        # Gera posições dos nós em círculo
        radius = min(WIDTH, HEIGHT) // 3
        center_x, center_y = WIDTH // 2, HEIGHT // 2 + 20
        
        for i in range(self.node_count):
            angle = 2 * math.pi * i / self.node_count
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            self.graph_nodes.append((int(x), int(y)))
        
        # Gera arestas aleatórias (grafo conectado)
        # Primeiro garante conectividade
        for i in range(self.node_count - 1):
            weight = random.randint(1, 20)
            self.graph_edges.append((i, i + 1, weight))
        
        # Adiciona arestas adicionais
        extra_edges = random.randint(self.node_count // 2, self.node_count)
        for _ in range(extra_edges):
            n1 = random.randint(0, self.node_count - 1)
            n2 = random.randint(0, self.node_count - 1)
            if n1 != n2 and not any(e[0] == n1 and e[1] == n2 or e[0] == n2 and e[1] == n1 for e in self.graph_edges):
                weight = random.randint(1, 20)
                self.graph_edges.append((n1, n2, weight))
        
        # Define nós inicial e final
        self.start_node = 0
        self.end_node = self.node_count - 1
        self.distances[self.start_node] = 0
        
        self.operation_count = 0
    
    def draw_graph(self):
        """Desenha o grafo com nós e arestas"""
        self.screen.fill(BLACK)
        
        # Desenha arestas
        font_small = pygame.font.Font(None, 18)
        for n1, n2, weight in self.graph_edges:
            x1, y1 = self.graph_nodes[n1]
            x2, y2 = self.graph_nodes[n2]
            
            # Cor da aresta - verifica ambas direções pois o grafo é não-direcionado
            is_in_path = False
            for i in range(len(self.path) - 1):
                a, b = self.path[i], self.path[i+1]
                if (n1 == a and n2 == b) or (n1 == b and n2 == a):
                    is_in_path = True
                    break
            
            if is_in_path:
                color = GREEN
                width = 4
            else:
                color = (100, 100, 100)
                width = 2
            
            pygame.draw.line(self.screen, color, (x1, y1), (x2, y2), width)
            
            # Desenha peso da aresta
            mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
            weight_text = font_small.render(str(weight), True, WHITE)
            self.screen.blit(weight_text, (mid_x - 10, mid_y - 10))
        
        # Desenha nós
        font_medium = pygame.font.Font(None, 24)
        for i, (x, y) in enumerate(self.graph_nodes):
            # Cor do nó
            if i == self.start_node:
                color = BLUE
            elif i == self.end_node:
                color = RED
            elif i == self.current_node:
                color = YELLOW
            elif i in self.visited_nodes:
                color = GREEN
            else:
                color = WHITE
            
            # Desenha círculo do nó
            pygame.draw.circle(self.screen, color, (x, y), 20)
            pygame.draw.circle(self.screen, BLACK, (x, y), 18)
            
            # Desenha número do nó
            node_text = font_medium.render(str(i), True, color)
            text_rect = node_text.get_rect(center=(x, y))
            self.screen.blit(node_text, text_rect)
            
            # Mostra distância se calculada
            if self.graph_category == 'global' and self.distances.get(i, float('inf')) != float('inf'):
                dist_text = font_small.render(f"d:{self.distances[i]}", True, YELLOW)
                self.screen.blit(dist_text, (x - 15, y + 25))
        
        # Texto de instrução
        font = pygame.font.Font(None, 28)
        title_text = font.render(f"SPACE: Pausar | R: Reset | ESC: Menu", True, WHITE)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 5))
        
        # Mostrar algoritmo atual
        font_medium = pygame.font.Font(None, 26)
        algo_text = font_medium.render(f"Algoritmo: {self.current_algorithm}", True, YELLOW)
        self.screen.blit(algo_text, (WIDTH // 2 - algo_text.get_width() // 2, 32))
        
        font_small = pygame.font.Font(None, 22)
        status = f"Operations: {self.operation_count} | Nodes: {self.node_count}"
        status_text = font_small.render(status, True, WHITE)
        self.screen.blit(status_text, (10, HEIGHT - 25))
        
        # Info de categoria
        category_name = "Global" if self.graph_category == 'global' else f"Local ({self.start_node} → {self.end_node})"
        category_text = font_small.render(category_name, True, LIGHT_GRAY)
        self.screen.blit(category_text, (WIDTH - category_text.get_width() - 10, HEIGHT - 25))
        
        pygame.display.flip()
    
    def dijkstra_visual(self):
        """Algoritmo de Dijkstra com visualização"""
        import heapq
        
        pq = [(0, self.start_node)]
        visited = set()
        parent = {i: None for i in range(self.node_count)}  # Para reconstruir caminho
        
        while pq and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            dist, node = heapq.heappop(pq)
            
            if node in visited:
                continue
            
            visited.add(node)
            self.visited_nodes.append(node)
            self.current_node = node
            self.operation_count += 1
            
            try:
                self.draw_graph()
                self.clock.tick(3)
            except:
                pass  # Ignora erros de desenho durante execução
            
            # Atualiza distâncias dos vizinhos
            for n1, n2, weight in self.graph_edges:
                neighbor = None
                if n1 == node:
                    neighbor = n2
                elif n2 == node:
                    neighbor = n1
                
                if neighbor is not None and neighbor not in visited:
                    new_dist = dist + weight
                    if new_dist < self.distances[neighbor]:
                        self.distances[neighbor] = new_dist
                        parent[neighbor] = node  # Armazena o pai
                        heapq.heappush(pq, (new_dist, neighbor))
            
            yield
        
        # Reconstrói o caminho do início ao fim
        self.path = []
        current = self.end_node
        while current is not None:
            self.path.insert(0, current)
            current = parent[current]
        
        self.current_node = -1
    
    def bellman_ford_visual(self):
        """Algoritmo de Bellman-Ford com visualização"""
        parent = {i: None for i in range(self.node_count)}  # Para reconstruir caminho
        
        # Relaxa todas as arestas V-1 vezes
        for iteration in range(self.node_count - 1):
            if not self.running:
                return
                
            for n1, n2, weight in self.graph_edges:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        return
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.running = False
                            return
                
                if not self.running:
                    return
                
                # Relaxamento bidirecional
                if self.distances[n1] + weight < self.distances[n2]:
                    self.distances[n2] = self.distances[n1] + weight
                    parent[n2] = n1  # Armazena o pai
                    self.current_node = n2
                    if n2 not in self.visited_nodes:
                        self.visited_nodes.append(n2)
                    
                    self.operation_count += 1
                    try:
                        self.draw_graph()
                        self.clock.tick(5)
                    except:
                        pass
                    yield
                
                if self.distances[n2] + weight < self.distances[n1]:
                    self.distances[n1] = self.distances[n2] + weight
                    parent[n1] = n2  # Armazena o pai
                    self.current_node = n1
                    if n1 not in self.visited_nodes:
                        self.visited_nodes.append(n1)
                    
                    self.operation_count += 1
                    try:
                        self.draw_graph()
                        self.clock.tick(5)
                    except:
                        pass
                    yield
        
        # Reconstrói o caminho do início ao fim
        self.path = []
        current = self.end_node
        while current is not None:
            self.path.insert(0, current)
            current = parent[current]
        
        self.current_node = -1
    
    def floyd_warshall_visual(self):
        """Algoritmo de Floyd-Warshall com visualização"""
        # Inicializa matriz de distâncias
        dist = [[float('inf')] * self.node_count for _ in range(self.node_count)]
        next_node = [[None] * self.node_count for _ in range(self.node_count)]  # Para reconstruir caminho
        
        for i in range(self.node_count):
            dist[i][i] = 0
        
        for n1, n2, weight in self.graph_edges:
            dist[n1][n2] = weight
            dist[n2][n1] = weight
            next_node[n1][n2] = n2
            next_node[n2][n1] = n1
        
        # Algoritmo principal
        for k in range(self.node_count):
            for i in range(self.node_count):
                for j in range(self.node_count):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            self.running = False
                            return
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                self.running = False
                                return
                    
                    if not self.running:
                        return
                    
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        next_node[i][j] = next_node[i][k]  # Atualiza próximo nó no caminho
                        
                        self.current_node = j
                        if j not in self.visited_nodes:
                            self.visited_nodes.append(j)
                        
                        self.operation_count += 1
                        
                        # Atualiza distâncias a partir do nó inicial
                        for idx in range(self.node_count):
                            self.distances[idx] = dist[self.start_node][idx]
                        
                        try:
                            self.draw_graph()
                            self.clock.tick(8)
                        except:
                            pass
                        yield
        
        # Reconstrói o caminho do início ao fim
        self.path = []
        if dist[self.start_node][self.end_node] != float('inf'):
            current = self.start_node
            self.path.append(current)
            while current != self.end_node:
                current = next_node[current][self.end_node]
                if current is None:
                    break
                self.path.append(current)
        
        self.current_node = -1
    
    def bfs_visual(self):
        """Busca em Largura (BFS) com visualização"""
        from collections import deque
        
        queue = deque([self.start_node])
        visited = {self.start_node}
        parent = {self.start_node: None}
        
        while queue:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            node = queue.popleft()
            self.current_node = node
            self.visited_nodes.append(node)
            self.operation_count += 1
            
            try:
                self.draw_graph()
                self.clock.tick(5)
            except:
                pass
            
            if node == self.end_node:
                # Reconstrói caminho
                self.path = []
                current = self.end_node
                while current is not None:
                    self.path.insert(0, current)
                    current = parent[current]
                break
            
            # Adiciona vizinhos não visitados
            for n1, n2, _ in self.graph_edges:
                neighbor = None
                if n1 == node and n2 not in visited:
                    neighbor = n2
                elif n2 == node and n1 not in visited:
                    neighbor = n1
                
                if neighbor is not None:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    queue.append(neighbor)
            
            yield
        
        self.current_node = -1
    
    def dfs_visual(self):
        """Busca em Profundidade (DFS) com visualização"""
        stack = [self.start_node]
        visited = {self.start_node}
        parent = {self.start_node: None}
        
        while stack:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            node = stack.pop()
            self.current_node = node
            self.visited_nodes.append(node)
            self.operation_count += 1
            
            try:
                self.draw_graph()
                self.clock.tick(5)
            except:
                pass
            
            if node == self.end_node:
                # Reconstrói caminho
                self.path = []
                current = self.end_node
                while current is not None:
                    self.path.insert(0, current)
                    current = parent[current]
                break
            
            # Adiciona vizinhos não visitados
            for n1, n2, _ in self.graph_edges:
                neighbor = None
                if n1 == node and n2 not in visited:
                    neighbor = n2
                elif n2 == node and n1 not in visited:
                    neighbor = n1
                
                if neighbor is not None:
                    visited.add(neighbor)
                    parent[neighbor] = node
                    stack.append(neighbor)
            
            yield
        
        self.current_node = -1
    
    def astar_visual(self):
        """A* com visualização (heurística: distância euclidiana)"""
        import heapq
        import math
        
        def heuristic(n1, n2):
            x1, y1 = self.graph_nodes[n1]
            x2, y2 = self.graph_nodes[n2]
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2) / 10
        
        pq = [(heuristic(self.start_node, self.end_node), 0, self.start_node)]
        visited = set()
        parent = {self.start_node: None}
        g_score = {i: float('inf') for i in range(self.node_count)}
        g_score[self.start_node] = 0
        
        while pq:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
            
            if not self.running:
                return
            
            _, g, node = heapq.heappop(pq)
            
            if node in visited:
                continue
            
            visited.add(node)
            self.current_node = node
            self.visited_nodes.append(node)
            self.operation_count += 1
            
            try:
                self.draw_graph()
                self.clock.tick(5)
            except:
                pass
            
            if node == self.end_node:
                # Reconstrói caminho
                self.path = []
                current = self.end_node
                while current is not None:
                    self.path.insert(0, current)
                    current = parent[current]
                break
            
            # Explora vizinhos
            for n1, n2, weight in self.graph_edges:
                neighbor = None
                if n1 == node:
                    neighbor = n2
                elif n2 == node:
                    neighbor = n1
                
                if neighbor is not None and neighbor not in visited:
                    tentative_g = g + weight
                    if tentative_g < g_score[neighbor]:
                        g_score[neighbor] = tentative_g
                        f_score = tentative_g + heuristic(neighbor, self.end_node)
                        parent[neighbor] = node
                        heapq.heappush(pq, (f_score, tentative_g, neighbor))
            
            yield
        
        self.current_node = -1
    
    def setup_array(self):
        """Configura o array com o tamanho escolhido"""
        # Gera valores com mais variação - usa range maior que o tamanho do array
        max_value = max(100, self.array_size * 2)  # Pelo menos 100, ou 2x o tamanho
        self.array = random.sample(range(1, max_value + 1), self.array_size)
        
        if self.algorithm_type == 'sorting':
            # Array já está embaralhado pelo random.sample
            pass
        elif self.algorithm_type == 'searching':
            # Para busca, precisa ordenar (exceto busca linear)
            if self.current_algorithm != 'Busca Linear':
                self.array.sort()
            # Busca linear mantém embaralhado
        
        self.bar_width = max(1, WIDTH // self.array_size)
        self.skip_frames = max(1, self.array_size // 500)
        self.comparing = []
        self.swapping = []
        self.sorted_indices = []
        self.operation_count = 0
        self.found_index = -1
        
        # Define alvo de busca aleatório (um dos valores do array)
        if self.algorithm_type == 'searching':
            self.search_target = random.choice(self.array)
    
    def run(self):
        """Loop principal"""
        sorting = False
        sort_generator = None
        paused = False
        
        while self.running:
            mouse_pos = pygame.mouse.get_pos()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                
                # Menu Principal
                if self.state == 'MENU':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.start_button.is_clicked(mouse_pos):
                            self.state = 'CHOOSE_TYPE'
                        elif self.quit_button.is_clicked(mouse_pos):
                            self.running = False
                
                # Escolha de Tipo
                elif self.state == 'CHOOSE_TYPE':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.sorting_type_button.is_clicked(mouse_pos):
                            self.algorithm_type = 'sorting'
                            self.state = 'SIZE_INPUT'
                        elif self.searching_type_button.is_clicked(mouse_pos):
                            self.algorithm_type = 'searching'
                            self.state = 'SIZE_INPUT'
                        elif self.graph_type_button.is_clicked(mouse_pos):
                            self.algorithm_type = 'graph'
                            self.state = 'GRAPH_CATEGORY'
                        elif self.type_back_button.is_clicked(mouse_pos):
                            self.state = 'MENU'
                
                # Escolha de Categoria de Grafo
                elif self.state == 'GRAPH_CATEGORY':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.global_graph_button.is_clicked(mouse_pos):
                            self.graph_category = 'global'
                            self.node_count = 10  # Define número padrão de nós
                            self.create_algorithm_buttons()
                            self.state = 'ALGORITHM_SELECT'
                        elif self.local_graph_button.is_clicked(mouse_pos):
                            self.graph_category = 'local'
                            self.node_count = 10  # Define número padrão de nós
                            self.create_algorithm_buttons()
                            self.state = 'ALGORITHM_SELECT'
                        elif self.graph_cat_back_button.is_clicked(mouse_pos):
                            self.state = 'CHOOSE_TYPE'
                
                # Input de Tamanho
                elif self.state == 'SIZE_INPUT':
                    if self.input_box.handle_event(event):
                        # Enter pressionado
                        size = self.input_box.get_value()
                        if 1 <= size <= 10000:
                            self.array_size = size
                            self.create_algorithm_buttons()
                            self.state = 'ALGORITHM_SELECT'
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.confirm_size_button.is_clicked(mouse_pos):
                            size = self.input_box.get_value()
                            if 1 <= size <= 10000:
                                self.array_size = size
                                self.create_algorithm_buttons()
                                self.state = 'ALGORITHM_SELECT'
                        elif self.back_button.is_clicked(mouse_pos):
                            self.state = 'CHOOSE_TYPE'
                
                # Seleção de Algoritmo
                elif self.state == 'ALGORITHM_SELECT':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.algorithm_type == 'sorting':
                            algorithms = self.sorting_algorithms
                        elif self.algorithm_type == 'searching':
                            algorithms = self.search_algorithms
                        else:  # graph
                            algorithms = self.graph_global_algorithms if self.graph_category == 'global' else self.graph_local_algorithms
                        
                        for name, button in self.algo_buttons:
                            if button.is_clicked(mouse_pos):
                                self.current_algorithm = name
                                
                                if self.algorithm_type == 'graph':
                                    self.running = True  # Garante que running está True
                                    self.setup_graph()
                                    self.state = 'GRAPH'
                                else:
                                    self.setup_array()
                                    self.state = 'SORTING' if self.algorithm_type == 'sorting' else 'SEARCHING'
                                
                                sorting = True
                                sort_generator = algorithms[name]()
                                break
                        
                        # Botão voltar
                        if self.algo_back_button.is_clicked(mouse_pos):
                            if self.algorithm_type == 'graph':
                                self.state = 'GRAPH_CATEGORY'
                            else:
                                self.state = 'SIZE_INPUT'
                
                # Durante a Ordenação/Busca/Grafo
                elif self.state == 'SORTING' or self.state == 'SEARCHING' or self.state == 'GRAPH':
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.state = 'MENU'
                            sorting = False
                            sort_generator = None
                        if event.key == pygame.K_SPACE:
                            paused = not paused
                        if event.key == pygame.K_r:
                            if self.algorithm_type == 'graph':
                                self.setup_graph()
                                algorithms = self.graph_global_algorithms if self.graph_category == 'global' else self.graph_local_algorithms
                            elif self.algorithm_type == 'sorting':
                                self.setup_array()
                                algorithms = self.sorting_algorithms
                            else:
                                self.setup_array()
                                algorithms = self.search_algorithms
                            
                            sorting = True
                            sort_generator = algorithms[self.current_algorithm]()
                            paused = False
            
            # Atualiza hover dos botões
            if self.state == 'MENU':
                self.start_button.check_hover(mouse_pos)
                self.quit_button.check_hover(mouse_pos)
                self.draw_menu()
            
            elif self.state == 'CHOOSE_TYPE':
                self.sorting_type_button.check_hover(mouse_pos)
                self.searching_type_button.check_hover(mouse_pos)
                self.graph_type_button.check_hover(mouse_pos)
                self.type_back_button.check_hover(mouse_pos)
                self.draw_choose_type()
            
            elif self.state == 'GRAPH_CATEGORY':
                self.global_graph_button.check_hover(mouse_pos)
                self.local_graph_button.check_hover(mouse_pos)
                self.graph_cat_back_button.check_hover(mouse_pos)
                self.draw_graph_category()
            
            elif self.state == 'SIZE_INPUT':
                self.confirm_size_button.check_hover(mouse_pos)
                self.back_button.check_hover(mouse_pos)
                self.draw_size_input()
            
            elif self.state == 'ALGORITHM_SELECT':
                for _, button in self.algo_buttons:
                    button.check_hover(mouse_pos)
                self.algo_back_button.check_hover(mouse_pos)
                self.draw_algorithm_select()
            
            elif self.state == 'SORTING' or self.state == 'SEARCHING' or self.state == 'GRAPH':
                if sorting and sort_generator and not paused:
                    try:
                        next(sort_generator)
                    except StopIteration:
                        sorting = False
                        # Animação de conclusão apenas para ordenação
                        if self.state == 'SORTING':
                            for i in range(len(self.array)):
                                self.sorted_indices.append(i)
                                self.play_sound(self.array[i])
                                self.draw()
                                self.clock.tick(FPS)
                                for event in pygame.event.get():
                                    if event.type == pygame.QUIT:
                                        self.running = False
                                    if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                        self.state = 'MENU'
                                        break
                
                if self.state == 'GRAPH':
                    self.draw_graph()
                else:
                    self.draw()
            
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    visualizer = SortingVisualizer()
    visualizer.run()
