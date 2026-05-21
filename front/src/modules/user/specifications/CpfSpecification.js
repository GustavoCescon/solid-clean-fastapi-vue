import { Specification } from "@/shared/specifications/Specification"

export class CpfValidSpecification extends Specification {
  isSatisfiedBy(cpf) {
    const digits = cpf.replace(/\D/g, "")

    if (digits.length !== 11 || /^(\d)\1+$/.test(digits)) return false

    for (let i = 9; i <= 10; i++) {
      let sum = 0
      for (let j = 0; j < i; j++) {
        sum += parseInt(digits[j]) * (i + 1 - j)
      }
      const digit = (sum * 10) % 11 % 10
      if (digit !== parseInt(digits[i])) return false
    }

    return true
  }
}

/**
 * Aplica a máscara CPF: "12345678909" → "123.456.789-09"
 * @param {string} value
 * @returns {string}
 */
export function maskCpf(value) {
  const digits = value.replace(/\D/g, "").slice(0, 11)
  return digits
    .replace(/^(\d{3})(\d)/, "$1.$2")
    .replace(/^(\d{3})\.(\d{3})(\d)/, "$1.$2.$3")
    .replace(/^(\d{3})\.(\d{3})\.(\d{3})(\d)/, "$1.$2.$3-$4")
}

/**
 * Remove a máscara do CPF: "123.456.789-09" → "12345678909"
 * @param {string} value
 * @returns {string}
 */
export function stripCpf(value) {
  return value.replace(/\D/g, "")
}
