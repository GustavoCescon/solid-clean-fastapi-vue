<template>
  <AppLayout>

    <div class="mb-6">
      <BaseButton
        icon="pi pi-arrow-left"
        label="Voltar"
        text
        size="small"
        class="mb-3"
        @click="router.push('/users')"
      />
      <h1 class="text-2xl font-bold text-surface-900">Novo Usuário</h1>
      <p class="text-surface-500 text-sm mt-0.5">Preencha os dados para criar um novo usuário</p>
    </div>

    <Card class="max-w-lg">
      <template #content>
        <Message v-if="error" severity="error" :closable="false" class="mb-4">
          {{ error }}
        </Message>
        <UserForm
          :name="name"
          :lastName="lastName"
          :cpf="cpf"
          :loading="loading"
          :errors="errors"
          @update:name="name = $event"
          @update:lastName="lastName = $event"
          @update:cpf="onCpfInput($event)"
          @submit="submit"
          @cancel="router.push('/users')"
        />
      </template>
    </Card>

  </AppLayout>
</template>

<script setup>
import { useRouter } from 'vue-router'
import AppLayout from '@/shared/components/layout/AppLayout.vue'
import UserForm from '../components/UserForm.vue'
import Card from 'primevue/card'
import BaseButton from '@/shared/components/base/BaseButton.vue'
import Message from 'primevue/message'
import { useCreateUserForm } from '../composables/useCreateUserForm'

const router = useRouter()
const { name, lastName, cpf, loading, error, submit, errors, onCpfInput } = useCreateUserForm()
</script>