<template>
  <div class="layout-wrapper">

    <!-- NAVBAR -->
    <header class="navbar">
      <div class="navbar-inner">

        <!-- Brand -->
        <router-link to="/" class="navbar-brand">
          <i class="pi pi-bolt navbar-brand-icon" />
          <span class="navbar-brand-name">App</span>
        </router-link>

        <!-- Nav links -->
        <nav class="navbar-nav">
          <router-link to="/users" class="nav-link" active-class="nav-link--active">
            <i class="pi pi-users" />
            <span>Users</span>
          </router-link>
          <router-link to="/users/create" class="nav-link" active-class="nav-link--active">
            <i class="pi pi-user-plus" />
            <span>Create</span>
          </router-link>
        </nav>

        <!-- Right side -->
        <div class="navbar-right">
          <button v-if="authStore.isAuthenticated" class="btn-logout" @click="handleLogout">
            <i class="pi pi-sign-out" />
            <span>Logout</span>
          </button>
        </div>

      </div>
    </header>

    <!-- CONTENT -->
    <main class="page-content">
      <slot />
    </main>

  </div>
</template>

<script setup>
import { authStore } from '@/modules/auth/store/authStore'
import { useRouter } from 'vue-router'

const router = useRouter()

function handleLogout() {
  authStore.logout()
  router.push('/login')
}
</script>

<style scoped>
.layout-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  background-color: var(--p-surface-50, #f8fafc);
}

/* ── Navbar ────────────────────────────────────────────────── */
.navbar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: var(--p-surface-0, #ffffff);
  border-bottom: 1px solid var(--p-surface-200, #e2e8f0);
  box-shadow: 0 1px 8px 0 rgba(0, 0, 0, 0.07);
}

.navbar-inner {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 1.5rem;
  height: 64px;
  display: flex;
  align-items: center;
  gap: 2rem;
}

/* Brand */
.navbar-brand {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  text-decoration: none;
  color: var(--p-primary-color, #6366f1);
  font-size: 1.2rem;
  font-weight: 700;
  letter-spacing: -0.5px;
  flex-shrink: 0;
}

.navbar-brand-icon {
  font-size: 1.3rem;
}

.navbar-brand-name {
  color: var(--p-surface-900, #0f172a);
}

/* Nav links */
.navbar-nav {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  flex: 1;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 0.9rem;
  border-radius: 8px;
  text-decoration: none;
  font-size: 0.9rem;
  font-weight: 500;
  color: var(--p-surface-600, #475569);
  transition: background 0.15s, color 0.15s;
}

.nav-link:hover {
  background: var(--p-surface-100, #f1f5f9);
  color: var(--p-surface-900, #0f172a);
}

.nav-link--active {
  background: var(--p-primary-50, #eef2ff);
  color: var(--p-primary-color, #6366f1);
  font-weight: 600;
}

/* Right side */
.navbar-right {
  margin-left: auto;
}

.btn-logout {
  display: flex;
  align-items: center;
  gap: 0.4rem;
  padding: 0.45rem 0.9rem;
  border: 1px solid var(--p-surface-200, #e2e8f0);
  border-radius: 8px;
  background: transparent;
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--p-surface-600, #475569);
  cursor: pointer;
  transition: background 0.15s, color 0.15s, border-color 0.15s;
}

.btn-logout:hover {
  background: #fef2f2;
  color: #ef4444;
  border-color: #fca5a5;
}

/* ── Page content ──────────────────────────────────────────── */
.page-content {
  flex: 1;
  max-width: 1280px;
  width: 100%;
  margin: 0 auto;
  padding: 2rem 1.5rem;
}
</style>