import { ref } from "vue"

import {
  getUsers,
  createUser,
  removeUserById,
} from "../services/userService"

import { useRequest } from "@/shared/composables/useRequest"

export function useUsers() {

  const users = ref([])
  const total = ref(0)
  const page = ref(1)
  const size = ref(10)

  const {
    loading,
    error,
    execute,
  } = useRequest()

  const fetchUsers = async () => {

    await execute(async () => {
      const data = await getUsers({ page: page.value, size: size.value })
      users.value = data.items
      total.value = data.total
    })
  }

  const onPage = async (event) => {
    page.value = event.page + 1
    size.value = event.rows
    await fetchUsers()
  }

  const saveUser = async (payload) => {

    return execute(() =>
      createUser(payload)
    )
  }

  const deleteUser = async (id) => {

    await execute(async () => {

      await removeUserById(id)

      await fetchUsers()
    })
  }

  return {
    users,
    total,
    page,
    size,

    loading,
    error,

    fetchUsers,
    onPage,
    saveUser,
    deleteUser,
  }
}