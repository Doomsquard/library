<template>
  <nav class="navbar headerComponent navbar-expand-lg navbar-light bg-white">
    <div class="container d-flex justify-content-between">
      <b-navbar toggleable="lg">
        <b-navbar-brand href="#"
          ><router-link class="navbar-brand d-flex" :to="{ path: '/library' }">
            <img
              width="50px"
              src="../assets/images/brainbook.svg"
              class="navbar-brand-img"
              alt="logo"
            />
            <p class="header__title">
              Your Library
            </p>
          </router-link></b-navbar-brand
        >

        <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

        <b-collapse id="nav-collapse" is-nav>
          <b-navbar-nav class="ml-auto">
            <b-nav-item
              @click="check"
              v-for="(book, index) in buttons"
              :key="book + index"
            >
              <router-link :to="{ name: book.name }" class="button__link">{{
                book.text
              }}</router-link>
            </b-nav-item>
            <b-nav-item @click="logoutHandler">
              <router-link :to="{ name: 'signInPage' }" class="button__link"
                >Logout</router-link
              >
            </b-nav-item>
          </b-navbar-nav>
        </b-collapse>
      </b-navbar>
    </div>
  </nav>
</template>

<script>
import { deleteCookie } from "../cookies/methods";
export default {
  name: "headerComponent",
  data() {
    return {
      buttons: [
        {
          name: "profilePage",
          text: "Profile"
        },
        {
          name: "libraryPage",
          text: "Library"
        },
        {
          name: "booksPage",
          text: "My books"
        },
        {
          name: "downloadPage",
          text: "Download"
        }
      ]
    };
  },
  methods: {
    check() {
      this.$store.dispatch("tokenModule/checkToken");
    },
    logoutHandler() {
      this.$store.dispatch("tokenModule/logoutUser");
      localStorage.removeItem("access_token");
      deleteCookie("jwtRefresh");
      this.$router.push({ name: "signInPage" });
    }
  }
};
</script>

<style lang="scss" scoped></style>

<style lang="scss" scoped>
.headerComponent {
  z-index: 99;
  &__title {
    font-size: 1.5rem;
  }
}
.headerComponent::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: 100%;
  height: 4px;
  background: linear-gradient(
    180deg,
    rgba(9, 30, 66, 0.13) 0,
    rgba(9, 30, 66, 0.13) 1px,
    rgba(9, 30, 66, 0.08) 1px,
    rgba(9, 30, 66, 0) 4px
  );
}

.navbar-expand-lg {
  min-width: 100%;
}

.navbar-nav {
  display: flex;
  align-items: flex-end;
}

#nav-collapse {
  text-decoration: none;
  color: black;
  &:hover {
    text-decoration: none;
  }
}

.button__link {
  text-decoration: none;
  z-index: 99;
  color: black;
  &:hover {
    text-decoration: none;
    box-shadow: 0 2px black;
  }
}
</style>
