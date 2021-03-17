<template>
  <div class="downloadPage">
    <router-view></router-view>
    <download-component />
  </div>
</template>

<script>
import DownloadComponent from "../components/downloadComponent.vue";

export default {
  name: "downloadPage",
  components: { DownloadComponent }
};
</script>

<style lang="scss" scoped>
.downloadPage {
  height: 100vh;
}
</style>
