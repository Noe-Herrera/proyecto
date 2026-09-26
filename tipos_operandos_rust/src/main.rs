fn calcular_oleadas(derrotados: i32, por_oleada: i32) -> i32 {
    derrotados / por_oleada
}

fn calcular_dano_critico(dano_base: i32, multiplicador: f64) -> f64 {
    dano_base as f64 * multiplicador
}

fn calcular_dano_promedio(dano_base: i32, por_oleada: i32) -> f64 {
    dano_base as f64 / por_oleada as f64
}

fn main() {
    println!("Oleadas completas: {}", calcular_oleadas(7, 2));
    println!("Daño crítico: {}", calcular_dano_critico(25, 1.5));
    println!("Daño promedio: {}", calcular_dano_promedio(25, 2));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn prueba_calcular_oleadas() {
        assert_eq!(calcular_oleadas(7, 2), 3);
    }

    #[test]
    fn prueba_calcular_dano_critico() {
        assert!((calcular_dano_critico(25, 1.5) - 37.5).abs() < 1e-10);
    }

    #[test]
    fn prueba_calcular_dano_promedio() {
        assert!((calcular_dano_promedio(25, 2) - 12.5).abs() < 1e-10);
    }
}
