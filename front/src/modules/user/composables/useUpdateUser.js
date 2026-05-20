import { ref } from "vue"
import { useRouter } from "vue-router"

import { getUserById, updateUser } from "../services/userService"

export function useUpdateUser() {
  const router = useRouter()

  const id = ref(null)

  const name = ref("")
  const email = ref("")
  const lastName = ref("")

  const loading = ref(false)
  const error = ref(null)

  const loadUser = async (userId) => {
    const user = await getUserById(userId)

    id.value = userId
    name.value = user.name
    email.value = user.email
    lastName.value = user.lastName
  }

  const update = async () => {
    loading.value = true
    error.value = null

    try {
      await updateUser(id.value, {
        name: name.value,
        email: email.value,
        lastName: lastName.value,
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

    loading,
    error,

    loadUser,
    update,
  }
}