import { reactive } from "vue"
import { UserService } from "../services/userService"

export const userStore = reactive({
  users: [],
  loading: false,

  async fetchUsers() {
    this.loading = true
    this.users = await UserService.list()
    this.loading = false
  },

  async createUser(payload) {
    await UserService.create(payload)
    await this.fetchUsers()
  },

  async deleteUser(id) {
    await UserService.delete(id)
    await this.fetchUsers()
  },
})