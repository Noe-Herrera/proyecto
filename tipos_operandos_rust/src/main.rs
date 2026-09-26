fn calcular_oleadas(derrotados: i32, por_oleada: i32) -> i32 {
    derrotados / por_oleada
}

fn calcular_dano_critico(dano_base: i32, multiplicador: f64) -> f64 {
    dano_base as f64 * multiplicador
}

fn main() {
    println!("Daño crítico: {}", calcular_dano_critico(25, 1.5));
    println!("Oleadas completas: {}", calcular_oleadas(7, 2));
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
}
