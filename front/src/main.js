import { createApp } from 'vue'
import App from './App.vue'

import PrimeVue from "primevue/config"
import './style.css'
import Aura from "@primevue/themes/aura"
import "primeicons/primeicons.css"
import ToastService from "primevue/toastservice"
import ConfirmationService from "primevue/confirmationservice"
import ConfirmDialog from "primevue/confirmdialog"
import Tooltip from "primevue/tooltip"

import router from './router'

const app = createApp(App)

app.use(PrimeVue, {
  theme: {
    preset: Aura,
  },
})
app.use(ToastService)
app.use(ConfirmationService)
app.use(router)
app.component("ConfirmDialog", ConfirmDialog)
app.directive("tooltip", Tooltip)
app.mount('#app')

