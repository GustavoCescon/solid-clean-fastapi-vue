import { ref } from "vue"

import { useRouter } from "vue-router"

import { useUsers } from "./useUsers"

import { z } from "zod"

import { CpfValidSpecification, maskCpf, stripCpf } from "../specifications/CpfSpecification"

const cpfSpec = new CpfValidSpecification()

const schema = z.object({
  name: z.string().min(1, "Nome é obrigatório"),
  lastName: z.string().min(1, "Sobrenome é obrigatório"),
  cpf: z
    .string()
    .min(14, "CPF inválido")
    .refine((val) => cpfSpec.isSatisfiedBy(val), { message: "CPF inválido" }),
})

export function useCreateUserForm() {
  const router = useRouter()

  const name = ref("")

  const lastName = ref("")

  const cpf = ref("")

  const errors = ref({})

  const {
    saveUser,
    loading,
    error,
  } = useUsers()

  const onCpfInput = (value) => {
    cpf.value = maskCpf(value)
  }

  const submit = async () => {
    const result = schema.safeParse({ name: name.value, lastName: lastName.value, cpf: cpf.value })

    if (!result.success) {
      errors.value = result.error.flatten().fieldErrors
      return
    }

    errors.value = {}

    try {
      await saveUser({
        name: name.value,
        lastName: lastName.value,
        cpf: stripCpf(cpf.value),
      })

      router.push("/users")
    } catch (error) {
      
    }
   
  }

  return {
    name,
    lastName,
    cpf,
    errors,
    loading,
    error,

    onCpfInput,
    submit,
  }
}