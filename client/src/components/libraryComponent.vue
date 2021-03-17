<template>
  <div class="wrapper container">
    aye
  </div>
</template>

<script>
import Header from "./header";

export default {
  name: "libraryComponent",
  components: { Header },
  created() {
    !localStorage.getItem("auth")
      ? this.$router.push({ path: "/signin" })
      : null;
  }
};
</script>

<style lang="scss" scoped>
.wrapper {
  position: absolute;
  top: 0;
  left: 0;
  margin-top: 100px;
}
</style>
