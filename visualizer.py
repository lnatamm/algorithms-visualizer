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
        self.state = 'MENU'  # MENU, SIZE_INPUT, ALGORITHM_SELECT, SORTING
        
        # Variáveis de configuração
        self.array_size = 100
        self.array = []
        self.bar_width = 0
        self.comparing = []
        self.swapping = []
        self.sorted_indices = []
        self.running = True
        self.sound_enabled = True
        self.operation_count = 0
        self.skip_frames = 1
        
        self.algorithms = {
            'QuickSort': self.quicksort_visual,
            'Merge Sort': self.mergesort_visual,
            'Heap Sort': self.heapsort_visual,
            'Bubble Sort': self.bubblesort_visual,
            'Insertion Sort': self.insertionsort_visual,
            'Selection Sort': self.selectionsort_visual,
            'Bogo Sort': self.bogosort_visual,
        }
        self.current_algorithm = 'QuickSort'
        
        # Componentes do menu
        self.init_menu_components()
    
    def init_menu_components(self):
        """Inicializa botões e elementos do menu"""
        # Menu principal
        self.start_button = Button(WIDTH//2 - 150, HEIGHT//2 - 50, 300, 80, "INICIAR", BLUE, HOVER_BLUE)
        self.quit_button = Button(WIDTH//2 - 150, HEIGHT//2 + 60, 300, 60, "Sair", RED, (255, 100, 100))
        
        # Input de tamanho
        self.input_box = InputBox(WIDTH//2 - 150, HEIGHT//2 - 40, 300, 80, '100')
        self.confirm_size_button = Button(WIDTH//2 - 150, HEIGHT//2 + 80, 300, 60, "Confirmar", GREEN, (0, 255, 100))
        self.back_button = Button(WIDTH//2 - 150, HEIGHT//2 + 160, 300, 50, "Voltar", LIGHT_GRAY, (220, 220, 220), BLACK)
        
        # Seleção de algoritmo
        self.algo_buttons = []
        algo_names = list(self.algorithms.keys())
        start_y = 150
        for i, name in enumerate(algo_names):
            button = Button(WIDTH//2 - 200, start_y + i * 68, 400, 58, name, PURPLE, (180, 0, 180))
            self.algo_buttons.append((name, button))
        
        # Botão voltar para seleção de algoritmo
        self.algo_back_button = Button(WIDTH//2 - 150, HEIGHT - 70, 300, 50, "Voltar", LIGHT_GRAY, (220, 220, 220), BLACK)
    
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
        title = font_large.render("Escolha o Algoritmo", True, YELLOW)
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
            bar_height = (value / self.array_size) * (HEIGHT - 100)
            y = HEIGHT - bar_height - 50
            
            # Determina a cor da barra
            if i in self.sorted_indices:
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
        font = pygame.font.Font(None, 36)
        title_text = font.render("SPACE: Pausar/Continuar | R: Reset | ESC: Menu", True, WHITE)
        self.screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 10))
        
        # Mostrar algoritmo atual
        font_medium = pygame.font.Font(None, 30)
        algo_text = font_medium.render(f"Algoritmo: {self.current_algorithm}", True, YELLOW)
        self.screen.blit(algo_text, (WIDTH // 2 - algo_text.get_width() // 2, 45))
        
        font_small = pygame.font.Font(None, 24)
        status = f"Operations: {self.operation_count} | Array Size: {self.array_size}"
        if self.sound_enabled:
            status += " | Sound: ON"
        else:
            status += " | Sound: OFF"
        
        status_text = font_small.render(status, True, WHITE)
        self.screen.blit(status_text, (10, HEIGHT - 30))
        
        pygame.display.flip()
        
    def play_sound(self, frequency):
        """Gera um som baseado na frequência (valor do elemento)"""
        if not self.sound_enabled:
            return
            
        # Mapeia o valor do array para uma frequência audível (200-2000 Hz)
        freq = int(200 + (frequency / self.array_size) * 1800)
        
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
    
    def setup_array(self):
        """Configura o array com o tamanho escolhido"""
        self.array = list(range(1, self.array_size + 1))
        random.shuffle(self.array)
        self.bar_width = max(1, WIDTH // self.array_size)
        self.skip_frames = max(1, self.array_size // 500)
        self.comparing = []
        self.swapping = []
        self.sorted_indices = []
        self.operation_count = 0
    
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
                            self.state = 'SIZE_INPUT'
                        elif self.quit_button.is_clicked(mouse_pos):
                            self.running = False
                
                # Input de Tamanho
                elif self.state == 'SIZE_INPUT':
                    if self.input_box.handle_event(event):
                        # Enter pressionado
                        size = self.input_box.get_value()
                        if 1 <= size <= 10000:
                            self.array_size = size
                            self.state = 'ALGORITHM_SELECT'
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.confirm_size_button.is_clicked(mouse_pos):
                            size = self.input_box.get_value()
                            if 1 <= size <= 10000:
                                self.array_size = size
                                self.state = 'ALGORITHM_SELECT'
                        elif self.back_button.is_clicked(mouse_pos):
                            self.state = 'MENU'
                
                # Seleção de Algoritmo
                elif self.state == 'ALGORITHM_SELECT':
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for name, button in self.algo_buttons:
                            if button.is_clicked(mouse_pos):
                                self.current_algorithm = name
                                self.setup_array()
                                self.state = 'SORTING'
                                sorting = True
                                sort_generator = self.algorithms[name]()
                                break
                        
                        # Botão voltar
                        if self.algo_back_button.is_clicked(mouse_pos):
                            self.state = 'SIZE_INPUT'
                
                # Durante a Ordenação
                elif self.state == 'SORTING':
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            self.state = 'MENU'
                            sorting = False
                            sort_generator = None
                        if event.key == pygame.K_SPACE:
                            paused = not paused
                        if event.key == pygame.K_r:
                            self.setup_array()
                            sorting = True
                            sort_generator = self.algorithms[self.current_algorithm]()
                            paused = False
            
            # Atualiza hover dos botões
            if self.state == 'MENU':
                self.start_button.check_hover(mouse_pos)
                self.quit_button.check_hover(mouse_pos)
                self.draw_menu()
            
            elif self.state == 'SIZE_INPUT':
                self.confirm_size_button.check_hover(mouse_pos)
                self.back_button.check_hover(mouse_pos)
                self.draw_size_input()
            
            elif self.state == 'ALGORITHM_SELECT':
                for _, button in self.algo_buttons:
                    button.check_hover(mouse_pos)
                self.algo_back_button.check_hover(mouse_pos)
                self.draw_algorithm_select()
            
            elif self.state == 'SORTING':
                if sorting and sort_generator and not paused:
                    try:
                        next(sort_generator)
                    except StopIteration:
                        sorting = False
                        # Inicia animação de conclusão
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
                
                self.draw()
            
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    visualizer = SortingVisualizer()
    visualizer.run()
