<template>
  <Form @submit="onSubmit" class="flex flex-col gap-4">

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4">

      <div class="flex flex-col gap-1.5 md:col-span-2">
        <label class="text-sm font-medium text-surface-700">Logradouro</label>
        <BaseInput :modelValue="street" @update:modelValue="emit('update:street', $event)" placeholder="Rua, Avenida..." />
      </div>

      <div class="flex flex-col gap-1.5">
        <label class="text-sm font-medium text-surface-700">Número</label>
        <BaseInput :modelValue="number" @update:modelValue="emit('update:number', $event)" placeholder="123" />
      </div>

      <div class="flex flex-col gap-1.5">
        <label class="text-sm font-medium text-surface-700">Complemento</label>
        <BaseInput :modelValue="complement" @update:modelValue="emit('update:complement', $event)" placeholder="Apto, Bloco..." />
      </div>

      <div class="flex flex-col gap-1.5">
        <label class="text-sm font-medium text-surface-700">Bairro</label>
        <BaseInput :modelValue="neighborhood" @update:modelValue="emit('update:neighborhood', $event)" placeholder="Bairro" />
      </div>

      <div class="flex flex-col gap-1.5">
        <label class="text-sm font-medium text-surface-700">CEP</label>
        <BaseInput :modelValue="zip_code" @update:modelValue="emit('update:zip_code', $event)" placeholder="00000-000" maxlength="9" />
      </div>

      <div class="flex flex-col gap-1.5">
        <label class="text-sm font-medium text-surface-700">Cidade</label>
        <BaseInput :modelValue="city" @update:modelValue="emit('update:city', $event)" placeholder="Cidade" />
      </div>

      <div class="flex flex-col gap-1.5">
        <label class="text-sm font-medium text-surface-700">Estado (UF)</label>
        <BaseInput :modelValue="state" @update:modelValue="emit('update:state', $event)" placeholder="SP" maxlength="2" />
      </div>

    </div>

    <div class="flex gap-2 pt-2">
      <BaseButton type="submit" label="Salvar" icon="pi pi-check" :loading="loading" />
      <BaseButton type="button" label="Cancelar" icon="pi pi-times" severity="secondary" @click="emit('cancel')" />
    </div>

  </Form>
</template>

<script setup>
import BaseInput from "@/shared/components/base/BaseInput.vue"
import BaseButton from "@/shared/components/base/BaseButton.vue"
import { Form } from "@primevue/forms"

const emit = defineEmits([
  "cancel", "submit",
  "update:street", "update:number", "update:complement",
  "update:neighborhood", "update:city", "update:state", "update:zip_code",
])

defineProps({
  street: String,
  number: String,
  complement: String,
  neighborhood: String,
  city: String,
  state: String,
  zip_code: String,
  loading: Boolean,
})

const onSubmit = () => emit("submit")
</script>
