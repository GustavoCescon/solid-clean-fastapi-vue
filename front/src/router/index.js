import { createRouter, createWebHistory } from "vue-router"

import LoginPage from "../modules/auth/pages/LoginPage.vue"
import UsersListPage from "../modules/user/pages/UsersListPage.vue"
import UsersCreatePage from "../modules/user/pages/UsersCreatePage.vue"
import RegisterPage from "../modules/auth/pages/RegisterPage.vue"
import UsersEditPage from "../modules/user/pages/UsersEditPage.vue"
import AddressListPage from "../modules/address/pages/AddressListPage.vue"
import AddressCreatePage from "../modules/address/pages/AddressCreatePage.vue"
import AddressEditPage from "../modules/address/pages/AddressEditPage.vue"

const routes = [
  { path: "/login", component: LoginPage },
  {
    path: "/register",
    component: RegisterPage,
  },
  {
    path: "/",
    redirect: () => {
      return localStorage.getItem("token") ? "/users" : "/login"
    },
  },

  {
    path: "/users",
    component: UsersListPage,
    meta: { requiresAuth: true },
  },

  {
    path: "/users/create",
    component: UsersCreatePage,
    meta: { requiresAuth: true },
  },
  {
    path: "/users/:userId/addresses",
    component: AddressListPage,
    meta: { requiresAuth: true },
  },
  {
    path: "/users/:userId/addresses/create",
    component: AddressCreatePage,
    meta: { requiresAuth: true },
  },
  {
    path: "/users/:userId/addresses/:addressId/edit",
    component: AddressEditPage,
    meta: { requiresAuth: true },
  },
  {
    path: "/users/:id/edit",
    component: UsersEditPage,
    meta: { requiresAuth: true },
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to) => {
  const isAuthenticated = !!localStorage.getItem("token")

  if (to.meta.requiresAuth && !isAuthenticated) {
    return "/login"
  }

  if (to.path === "/login" && isAuthenticated) {
    return "/users"
  }

  return true
})

export default router