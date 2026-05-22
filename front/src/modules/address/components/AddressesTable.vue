<template>
  <DataTable :value="addresses" stripedRows tableStyle="min-width: 40rem">

    <Column field="street" header="Logradouro" />
    <Column field="number" header="Número" style="width: 6rem" />
    <Column field="neighborhood" header="Bairro" />
    <Column field="city" header="Cidade" />
    <Column field="state" header="UF" style="width: 4rem" />
    <Column field="zip_code" header="CEP" style="width: 7rem" />

    <Column header="Ações" style="width: 9rem">
      <template #body="{ data }">
        <div class="flex gap-1">
          <BaseButton
            icon="pi pi-pencil"
            severity="info"
            size="small"
            rounded
            text
            v-tooltip.top="'Editar'"
            @click="emit('edit', data.id)"
          />
          <BaseButton
            icon="pi pi-trash"
            severity="danger"
            size="small"
            rounded
            text
            v-tooltip.top="'Deletar'"
            @click="emit('delete', data.id)"
          />
        </div>
      </template>
    </Column>

  </DataTable>
</template>

<script setup>
import DataTable from "primevue/datatable"
import Column from "primevue/column"
import BaseButton from "@/shared/components/base/BaseButton.vue"

defineProps({ addresses: Array })

const emit = defineEmits(["edit", "delete"])
</script>
