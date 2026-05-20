import { ref } from "vue"

import { useRouter } from "vue-router"

import { useUsers } from "./useUsers"

import { z } from "zod"

const schema = z.object({
  name: z.string().min(1, "Nome é obrigatório"),
  lastName: z.string().min(1, "Sobrenome é obrigatório"),
})

export function useCreateUserForm() {
  const router = useRouter()

  const name = ref("")

  const lastName = ref("")

  const errors = ref({})

  const {
    saveUser,
    loading,
    error,
  } = useUsers()

  const submit = async () => {
    const result = schema.safeParse({ name: name.value, lastName: lastName.value })

    if (!result.success) {
      errors.value = result.error.flatten().fieldErrors
      return
    }

    errors.value = {}

    try {
      await saveUser({
        name: name.value,
        lastName: lastName.value,
      })

      router.push("/users")
    } catch (error) {
      
    }
   
  }

  return {
    name,
    lastName,
    errors,
    loading,
    error,

    submit,
  }
}