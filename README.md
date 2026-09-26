# Operandos con Rust y pruebas unitarias

Actividad de Semana4 realizada en el repositorio del curso.

## Bitácora

### Paso 0 — Crear el branch y el proyecto con Cargo

- Partí de `main` actualizado con `git pull --ff-only` y creé `Semana4`.
- Creé el proyecto con `cargo new tipos_operandos_rust`.
- Agregué `**/target` al `.gitignore` de la raíz.
- Ejecuté `cargo run` desde `tipos_operandos_rust/`: compiló correctamente y mostró `Hello, world!`.
- Cargo conserva el repositorio existente: el proyecto no contiene un `.git` propio.

### Paso 1 — Primera prueba: calcular_oleadas

- Implementé `calcular_oleadas(derrotados: i32, por_oleada: i32) -> i32` mediante división entera.
- Agregué una sola prueba: `calcular_oleadas(7, 2) == 3`.
- Ejecuté `cargo test`: **1 passed; 0 failed**.
- Actualicé `main()` y comprobé con `cargo run` la salida `Oleadas completas: 3`.
