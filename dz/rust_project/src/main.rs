// Импорт необходимых библиотек
use serde::{Deserialize, Serialize};
use serde_json;
use std::fs;
use std::io;
use chrono::prelude::*;

// Структура задачи
#[derive(Debug, Serialize, Deserialize, Clone)]
struct Task {
    id: u32,
    title: String,
    description: String,
    completed: bool,
    created_at: String,
    completed_at: Option<String>,
}

// Структура менеджера задач
struct TaskManager {
    tasks: Vec<Task>,
    next_id: u32,
}

impl TaskManager {
    // Создание нового менеджера задач
    fn new() -> Self {
        TaskManager {
            tasks: Vec::new(),
            next_id: 1,
        }
    }

    // Добавление новой задачи
    fn add_task(&mut self, title: String, description: String) {
        let task = Task {
            id: self.next_id,
            title,
            description,
            completed: false,
            created_at: Local::now().to_rfc3339(),
            completed_at: None,
        };

        self.tasks.push(task);
        self.next_id += 1;
        println!("Задача успешно добавлена!");
    }

    // Просмотр всех задач
    fn view_tasks(&self) {
        if self.tasks.is_empty() {
            println!("Список задач пуст.");
            return;
        }

        println!("\n=== СПИСОК ЗАДАЧ ===");
        for task in &self.tasks {
            let status = if task.completed { "✓" } else { "✗" };
            println!("ID: {}", task.id);
            println!("Заголовок: {}", task.title);
            println!("Описание: {}", task.description);
            println!("Статус: {}", status);
            println!("Создана: {}", task.created_at);
            if let Some(completed_at) = &task.completed_at {
                println!("Завершена: {}", completed_at);
            }
            println!("---");
        }
    }

    // Отметка задачи как выполненной
    fn complete_task(&mut self, id: u32) -> Result<(), String> {
        for task in &mut self.tasks {
            if task.id == id {
                if !task.completed {
                    task.completed = true;
                    task.completed_at = Some(Local::now().to_rfc3339());
                    return Ok(());
                } else {
                    return Err("Задача уже выполнена".to_string());
                }
            }
        }
        Err("Задача с указанным ID не найдена".to_string())
    }

    // Удаление задачи
    fn delete_task(&mut self, id: u32) -> Result<(), String> {
        let initial_len = self.tasks.len();
        self.tasks.retain(|task| task.id != id);

        if self.tasks.len() < initial_len {
            Ok(())
        } else {
            Err("Задача с указанным ID не найдена".to_string())
        }
    }

    // Сохранение задач в файл
    fn save_to_file(&self, filename: &str) -> io::Result<()> {
        let json = serde_json::to_string_pretty(&self.tasks)?;
        fs::write(filename, json)?;
        println!("Задачи сохранены в файл '{}'", filename);
        Ok(())
    }

    // Загрузка задач из файла
    fn load_from_file(&mut self, filename: &str) -> io::Result<()> {
        let data = fs::read_to_string(filename)?;
        let tasks: Vec<Task> = serde_json::from_str(&data)?;

        // Находим максимальный ID для продолжения нумерации
        self.next_id = tasks.iter().map(|t| t.id).max().unwrap_or(0) + 1;
        self.tasks = tasks;
        println!("Задачи загружены из файла '{}'", filename);
        Ok(())
    }
}

// Главная функция
fn main() {
    println!("=== СИСТЕМА УПРАВЛЕНИЯ ЗАДАЧАМИ ===");

    let mut task_manager = TaskManager::new();
    let filename = "tasks.json";

    // Попытка загрузить задачи из файла при запуске
    if let Err(e) = task_manager.load_from_file(filename) {
        println!("Не удалось загрузить задачи: {}. Будет создан новый список.", e);
    }

    loop {
        println!("\nМеню:");
        println!("1. Добавить задачу");
        println!("2. Просмотреть задачи");
        println!("3. Завершить задачу");
        println!("4. Удалить задачу");
        println!("5. Сохранить задачи");
        println!("6. Выход");
        println!("Выберите действие: ");

        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Ошибка чтения ввода");

        match choice.trim() {
            "1" => {
                println!("Введите заголовок задачи: ");
                let mut title = String::new();
                io::stdin().read_line(&mut title).expect("Ошибка чтения ввода");

                println!("Введите описание задачи: ");
                let mut description = String::new();
                io::stdin().read_line(&mut description).expect("Ошибка чтения ввода");

                task_manager.add_task(
                    title.trim().to_string(),
                    description.trim().to_string()
                );
            }

            "2" => {
                task_manager.view_tasks();
            }

            "3" => {
                println!("Введите ID задачи для завершения: ");
                let mut id_input = String::new();
                io::stdin().read_line(&mut id_input).expect("Ошибка чтения ввода");

                match id_input.trim().parse::<u32>() {
                    Ok(id) => {
                        match task_manager.complete_task(id) {
                            Ok(_) => println!("Задача {} отмечена как выполненная!", id),
                            Err(e) => println!("Ошибка: {}", e),
                        }
                    }
                    Err(_) => println!("Неверный формат ID"),
                }
            }

            "4" => {
                println!("Введите ID задачи для удаления: ");
                let mut id_input = String::new();
                io::stdin().read_line(&mut id_input).expect("Ошибка чтения ввода");

                match id_input.trim().parse::<u32>() {
                    Ok(id) => {
                        match task_manager.delete_task(id) {
                            Ok(_) => println!("Задача {} удалена!", id),
                            Err(e) => println!("Ошибка: {}", e),
                        }
                    }
                    Err(_) => println!("Неверный формат ID"),
                }
            }

            "5" => {
                if let Err(e) = task_manager.save_to_file(filename) {
                    println!("Ошибка при сохранении: {}", e);
                }
            }

            "6" => {
                // Автосохранение при выходе
                if let Err(e) = task_manager.save_to_file(filename) {
                    println!("Ошибка при автосохранении: {}", e);
                }
                println!("До свидания!");
                break;
            }

            _ => {
                println!("Неверный выбор. Попробуйте снова.");
            }
        }
    }
}

// Тесты
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_add_task() {
        let mut manager = TaskManager::new();
        manager.add_task("Тест".to_string(), "Описание теста".to_string());

        assert_eq!(manager.tasks.len(), 1);
        assert_eq!(manager.tasks[0].title, "Тест");
        assert_eq!(manager.next_id, 2);
    }

    #[test]
    fn test_complete_task() {
        let mut manager = TaskManager::new();
        manager.add_task("Тест".to_string(), "Описание".to_string());

        let result = manager.complete_task(1);
        assert!(result.is_ok());
        assert!(manager.tasks[0].completed);
    }

    #[test]
    fn test_delete_task() {
        let mut manager = TaskManager::new();
        manager.add_task("Тест".to_string(), "Описание".to_string());

        let result = manager.delete_task(1);
        assert!(result.is_ok());
        assert!(manager.tasks.is_empty());
    }
}
