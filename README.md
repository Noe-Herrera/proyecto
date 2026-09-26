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

### Paso 2 — Segunda prueba: calcular_dano_critico

- Agregué `calcular_dano_critico(dano_base: i32, multiplicador: f64) -> f64`, convirtiendo `dano_base` con `as f64` antes de multiplicar.
- Conservé la prueba anterior y añadí el caso `25 * 1.5 = 37.5`, con tolerancia de `1e-10` para comparar valores `f64`.
- Ejecuté `cargo test`: **2 passed; 0 failed**.
- Actualicé `main()` y ejecuté `cargo run`: también muestra `Daño crítico: 37.5`.

### Paso 3 — Tercera prueba: calcular_dano_promedio

- Agregué `calcular_dano_promedio(dano_base: i32, por_oleada: i32) -> f64`.
- Convertí ambos operandos a `f64` antes de dividir para conservar la parte decimal.
- Añadí el caso `25 / 2 = 12.5`, con tolerancia de `1e-10`, sin modificar las dos pruebas anteriores.
- Ejecuté `cargo test`: **3 passed; 0 failed**.
- Actualicé `main()` para imprimir las tres funciones y ejecuté `cargo run`: oleadas `3`, daño crítico `37.5` y daño promedio `12.5`.
