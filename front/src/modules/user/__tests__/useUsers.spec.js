import { describe, it, expect, vi, beforeEach } from 'vitest'

vi.mock('../services/userService', () => ({
  getUsers: vi.fn(),
  createUser: vi.fn(),
  removeUserById: vi.fn(),
}))

import { getUsers, createUser, removeUserById } from '../services/userService'
import { useUsers } from '../composables/useUsers'

describe('useUsers', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('fetchUsers populates users and total', async () => {
    getUsers.mockResolvedValue({ items: [{ id: 1, name: 'Alice' }], total: 1 })

    const { users, total, fetchUsers } = useUsers()
    await fetchUsers()

    expect(users.value).toEqual([{ id: 1, name: 'Alice' }])
    expect(total.value).toBe(1)
  })

  it('fetchUsers uses current page and size', async () => {
    getUsers.mockResolvedValue({ items: [], total: 0 })

    const { fetchUsers } = useUsers()
    await fetchUsers()

    expect(getUsers).toHaveBeenCalledWith({ page: 1, size: 10 })
  })

  it('saveUser calls createUser with payload and returns result', async () => {
    const created = { id: 2, name: 'Bob', lastName: 'Jones' }
    createUser.mockResolvedValue(created)

    const { saveUser } = useUsers()
    const result = await saveUser({ name: 'Bob', lastName: 'Jones' })

    expect(createUser).toHaveBeenCalledWith({ name: 'Bob', lastName: 'Jones' })
    expect(result).toEqual(created)
  })

  it('deleteUser calls removeUserById then refreshes list', async () => {
    removeUserById.mockResolvedValue({})
    getUsers.mockResolvedValue({ items: [], total: 0 })

    const { deleteUser, users } = useUsers()
    await deleteUser(1)

    expect(removeUserById).toHaveBeenCalledWith(1)
    expect(getUsers).toHaveBeenCalled()
    expect(users.value).toEqual([])
  })

  it('onPage updates page and size then fetches', async () => {
    getUsers.mockResolvedValue({ items: [], total: 0 })

    const { onPage, page, size } = useUsers()
    await onPage({ page: 1, rows: 25 })

    expect(page.value).toBe(2)
    expect(size.value).toBe(25)
    expect(getUsers).toHaveBeenCalledWith({ page: 2, size: 25 })
  })

  it('loading is false after fetchUsers resolves', async () => {
    getUsers.mockResolvedValue({ items: [], total: 0 })

    const { fetchUsers, loading } = useUsers()
    await fetchUsers()

    expect(loading.value).toBe(false)
  })
})
