import { describe, it, expect, vi, beforeEach } from 'vitest'
import { AppError } from '@/shared/errors/AppError'

vi.mock('@/shared/api/http', () => ({
  default: {
    get: vi.fn(),
    post: vi.fn(),
    put: vi.fn(),
    delete: vi.fn(),
  },
}))

import api from '@/shared/api/http'
import {
  getUsers,
  createUser,
  getUserById,
  updateUser,
  removeUserById,
} from '../services/userService'

describe('userService', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  describe('getUsers', () => {
    it('returns paginated data', async () => {
      api.get.mockResolvedValue({
        data: { items: [{ id: 1, name: 'Alice' }], total: 1 },
      })

      const result = await getUsers({ page: 1, size: 10 })

      expect(api.get).toHaveBeenCalledWith('/users', { params: { page: 1, size: 10 } })
      expect(result.items).toHaveLength(1)
      expect(result.total).toBe(1)
    })

    it('uses default pagination params', async () => {
      api.get.mockResolvedValue({ data: { items: [], total: 0 } })

      await getUsers()

      expect(api.get).toHaveBeenCalledWith('/users', { params: { page: 1, size: 10 } })
    })

    it('throws AppError on failure', async () => {
      api.get.mockRejectedValue({
        response: { data: { error: 'Erro no servidor' }, status: 500 },
      })

      await expect(getUsers()).rejects.toBeInstanceOf(AppError)
    })
  })

  describe('createUser', () => {
    it('posts payload and returns created user', async () => {
      const user = { id: 1, name: 'Alice', lastName: 'Smith' }
      api.post.mockResolvedValue({ data: user })

      const result = await createUser({ name: 'Alice', lastName: 'Smith' })

      expect(api.post).toHaveBeenCalledWith('/users', { name: 'Alice', lastName: 'Smith' })
      expect(result).toEqual(user)
    })

    it('throws AppError on failure', async () => {
      api.post.mockRejectedValue({
        response: { data: { error: 'Erro ao criar' }, status: 400 },
      })

      await expect(createUser({ name: 'X' })).rejects.toBeInstanceOf(AppError)
    })
  })

  it('getUserById returns user data', async () => {
    api.get.mockResolvedValue({ data: { id: 1, name: 'Bob' } })

    const result = await getUserById(1)

    expect(api.get).toHaveBeenCalledWith('/users/1')
    expect(result.name).toBe('Bob')
  })

  it('updateUser sends put request and returns updated data', async () => {
    api.put.mockResolvedValue({ data: { id: 1, name: 'Updated', lastName: 'X' } })

    const result = await updateUser(1, { name: 'Updated', lastName: 'X' })

    expect(api.put).toHaveBeenCalledWith('/users/1', { name: 'Updated', lastName: 'X' })
    expect(result.name).toBe('Updated')
  })

  it('removeUserById sends delete request', async () => {
    api.delete.mockResolvedValue({ data: { message: 'Deleted' } })

    const result = await removeUserById(1)

    expect(api.delete).toHaveBeenCalledWith('/users/1')
    expect(result.message).toBe('Deleted')
  })
})
