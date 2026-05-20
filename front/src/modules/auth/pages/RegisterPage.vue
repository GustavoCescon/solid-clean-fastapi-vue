<template>
  <div class="min-h-screen flex items-center justify-center bg-surface-50">
    <Card class="w-full max-w-sm shadow-2xl">

      <template #header>
        <div class="flex flex-col items-center pt-8 pb-2 px-6">
          <div class="w-14 h-14 rounded-2xl bg-primary flex items-center justify-center mb-4 shadow-md">
            <i class="pi pi-user-plus text-white text-2xl" />
          </div>
          <h1 class="text-2xl font-bold text-surface-900">Criar Conta</h1>
          <p class="text-surface-500 text-sm mt-1">Preencha os dados para se registrar</p>
        </div>
      </template>

      <template #content>
        <form @submit.prevent="submit" class="flex flex-col gap-4">

          <div class="flex flex-col gap-1.5">
            <label class="text-sm font-medium text-surface-700">Login</label>
            <BaseInput
              v-model="login"
              placeholder="nome de usuário"
            />
          </div>

          <div class="flex flex-col gap-1.5">
            <label class="text-sm font-medium text-surface-700">Email</label>
            <BaseInput
              v-model="email"
              type="email"
              placeholder="seu@email.com"
            />
          </div>

          <div class="flex flex-col gap-1.5">
            <label class="text-sm font-medium text-surface-700">Senha</label>
            <Password
              v-model="password"
              placeholder="••••••••"
              toggleMask
              fluid
            />
          </div>

          <Message v-if="error" severity="error" :closable="false" class="mt-1">
            {{ error }}
          </Message>

          <BaseButton
            type="submit"
            label="Criar conta"
            icon="pi pi-check"
            :loading="loading"
            class="w-full mt-1"
          />

        </form>
      </template>

      <template #footer>
        <div class="text-center text-sm text-surface-500 pb-4">
          Já tem conta?
          <router-link to="/login" class="text-primary font-semibold hover:underline ml-1">
            Entrar
          </router-link>
        </div>
      </template>

    </Card>
  </div>
</template>

<script setup>
import Card from 'primevue/card'
import BaseInput from '@/shared/components/base/BaseInput.vue'
import Password from 'primevue/password'
import BaseButton from '@/shared/components/base/BaseButton.vue'
import Message from 'primevue/message'

import { useRegisterForm } from '../composables/useRegisterForm'

const { login, email, password, loading, error, submit } = useRegisterForm()
</script>