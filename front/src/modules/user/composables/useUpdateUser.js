import { ref } from "vue"
import { useRouter } from "vue-router"

import { getUserById, updateUser } from "../services/userService"
import { maskCpf, stripCpf } from "../specifications/CpfSpecification"

export function useUpdateUser() {
  const router = useRouter()

  const id = ref(null)

  const name = ref("")
  const email = ref("")
  const lastName = ref("")
  const cpf = ref("")

  const loading = ref(false)
  const error = ref(null)

  const loadUser = async (userId) => {
    const user = await getUserById(userId)

    id.value = userId
    name.value = user.name
    email.value = user.email
    lastName.value = user.lastName
    cpf.value = user.cpf ? maskCpf(user.cpf) : ""
  }

  const onCpfInput = (value) => {
    cpf.value = maskCpf(value)
  }

  const update = async () => {
    loading.value = true
    error.value = null

    try {
      await updateUser(id.value, {
        name: name.value,
        email: email.value,
        lastName: lastName.value,
        cpf: stripCpf(cpf.value),
      })

      router.push("/users")

    } catch (err) {
      error.value = err.message
    } finally {
      loading.value = false
    }
  }

  return {
    name,
    email,
    lastName,
    cpf,

    loading,
    error,

    loadUser,
    onCpfInput,
    update,
  }
}