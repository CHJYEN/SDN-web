<template>
  <NConfigProvider
    :theme="darkTheme"
    :theme-overrides="themeOverrides"
    class="overflow-y-auto font-mono"
  >
    <div class="h-screen font-major bg-bottom flex text-white text-base">
      <RouterView class="flex-1 h-full overflow-hidden" />
    </div>
  </NConfigProvider>
</template>

<script setup>
import { ref } from "vue";
import { NConfigProvider, darkTheme } from "naive-ui";
import { primaryColor, secondaryColor } from "./color";
/**
 * @type import('naive-ui').GlobalThemeOverrides
 */
const themeOverrides = {
  common: {
    primaryColor,
    primaryColorHover: "#BFE8FFFF",
    primaryColorPressed: "#4190BCFF",
    primaryColorSuppl: "#296E95FF",
  },
  Table: {
    tdColor: "rgba(0,0,0,0)",
    thColor: secondaryColor,
  },
  DataTable: {
    tdColor: "rgba(0,0,0,0)",
    thColor: secondaryColor,
    tdColorHover: "rgb(133,199,236,0.3)",
  },
};

const navs = ref([
  {
    path: "/",
    label: "SDN拓扑前端",
    icon: '<i class="ri-brain-line text-3xl"></i>',
  },
  
]);

const closed = ref(false);
</script>

<style>
a.router-link-exact-active {
  @apply bg-gradient-to-br from-primary to-secondary font-bold text-active;
}

.ab-center {
  @apply absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2;
}
</style>
