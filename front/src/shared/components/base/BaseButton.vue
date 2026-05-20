<template>
  <Button v-bind="$attrs">
    <template v-if="$slots.default" #default>
      <slot />
    </template>
  </Button>
</template>

<script setup>
import Button from 'primevue/button'
</script>