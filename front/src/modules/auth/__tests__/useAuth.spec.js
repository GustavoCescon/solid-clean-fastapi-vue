import { describe, it, expect, vi, beforeEach } from 'vitest'

const mockPush = vi.fn()

vi.mock('vue-router', () => ({
  useRouter: () => ({ push: mockPush }),
}))

vi.mock('../services/authService', () => ({
  login: vi.fn(),
  register: vi.fn(),
}))

vi.mock('../store/authStore', () => ({
  authStore: {
    token: null,
    isAuthenticated: false,
    setToken: vi.fn(),
    logout: vi.fn(),
  },
}))

import { useAuth } from '../composables/useAuth'
import { login, register } from '../services/authService'
import { authStore } from '../store/authStore'

describe('useAuth', () => {
  beforeEach(() => {
    vi.clearAllMocks()
  })

  it('signIn calls login with credentials, sets token and redirects to /users', async () => {
    login.mockResolvedValue({ access_token: 'token123' })

    const { signIn } = useAuth()
    await signIn('test@mail.com', 'pass')

    expect(login).toHaveBeenCalledWith({ email: 'test@mail.com', password: 'pass' })
    expect(authStore.setToken).toHaveBeenCalledWith('token123')
    expect(mockPush).toHaveBeenCalledWith('/users')
  })

  it('signUp calls register with credentials and redirects to /login', async () => {
    register.mockResolvedValue({})

    const { signUp } = useAuth()
    await signUp('testuser', 'test@mail.com', 'pass')

    expect(register).toHaveBeenCalledWith({
      login: 'testuser',
      email: 'test@mail.com',
      password: 'pass',
    })
    expect(mockPush).toHaveBeenCalledWith('/login')
  })

  it('logout clears store and redirects to /login', () => {
    const { logout } = useAuth()
    logout()

    expect(authStore.logout).toHaveBeenCalled()
    expect(mockPush).toHaveBeenCalledWith('/login')
  })

  it('signIn sets loading to false after request', async () => {
    login.mockResolvedValue({ access_token: 'abc' })

    const { signIn, loading } = useAuth()
    await signIn('a@b.com', 'pass')

    expect(loading.value).toBe(false)
  })

  it('signIn exposes error when login fails', async () => {
    login.mockRejectedValue(new Error('Credenciais inválidas'))

    const { signIn, error } = useAuth()

    await expect(signIn('bad@mail.com', 'wrong')).rejects.toThrow()
    expect(error.value).not.toBeNull()
  })
})
