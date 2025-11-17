list_notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']

# Добавляем мажорные ноты (с диезами)
major_notes = ['C#', 'D#', 'F#', 'G#', 'A#']

# Объединяем списки
all_notes = list_notes + major_notes

# Сортируем для правильного музыкального порядка
all_notes_sorted = sorted(all_notes, key=lambda x: (x[0], len(x)))

print("Исходный список:", list_notes)
print("Все ноты:", all_notes_sorted)