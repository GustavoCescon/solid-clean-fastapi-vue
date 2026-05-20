<template>
  <div class="min-h-screen flex items-center justify-center bg-surface-50">
    <Card class="w-full max-w-sm shadow-2xl">

      <template #header>
        <div class="flex flex-col items-center pt-8 pb-2 px-6">
          <div class="w-14 h-14 rounded-2xl bg-primary flex items-center justify-center mb-4 shadow-md">
            <i class="pi pi-bolt text-white text-2xl" />
          </div>
          <h1 class="text-2xl font-bold text-surface-900">Bem-vindo</h1>
          <p class="text-surface-500 text-sm mt-1">Faça login para continuar</p>
        </div>
      </template>

      <template #content>
        <form @submit.prevent="submit" class="flex flex-col gap-4">

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
              :feedback="false"
              toggleMask
              fluid
            />
          </div>

          <Message v-if="error" severity="error" :closable="false" class="mt-1">
            {{ error }}
          </Message>

          <BaseButton
            type="submit"
            label="Entrar"
            icon="pi pi-sign-in"
            :loading="loading"
            class="w-full mt-1"
          />

        </form>
      </template>

      <template #footer>
        <div class="text-center text-sm text-surface-500 pb-4">
          Não tem conta?
          <router-link to="/register" class="text-primary font-semibold hover:underline ml-1">
            Criar conta
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

import { useLoginForm } from '../composables/useLoginForm'

const { email, password, loading, error, submit } = useLoginForm()
</script>