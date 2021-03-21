<template>
  <div class="wrapper container">
    <loader v-if="loading" />
    <div v-else>
      <div class="container mt-5 d-flex justify-content-center">
        <div class="card p-3">
          <div class="d-flex align-items-center">
            <div class="ml-3 w-100">
              <h4 class="mb-0 mt-0">{{ login }}</h4>
              <span>Reader</span>
              <div
                class="p-2 mt-2 bg-primary d-flex justify-content-between rounded text-white stats"
              >
                <div class="d-flex flex-column">
                  <span class="articles">Age</span>
                  <span class="number1">{{ ageHandler }}</span>
                </div>
                <div class="d-flex flex-column">
                  <span class="followers">Want read</span>
                  <span class="number2">{{ wantRead }}</span>
                </div>
                <div class="d-flex flex-column">
                  <span class="rating">Readed</span>
                  <span class="number3">{{ readed }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="bookList__wrapper">
        <books-list
          title="FAVORIT BOOKS"
          :list="favbooks"
          currentId="1"
          place="book"
        />
        <books-list
          title="FAVORIT GENRE"
          :list="favgenre"
          currentId="2"
          place="genre"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Api from "../axios/index";
import booksList from "./booksList.vue";
import loader from "./loader.vue";

export default {
  components: { booksList, loader },
  name: "profileComponent",
  data() {
    return {
      login: "",
      favbooks: [],
      favgenre: [],
      wantRead: "",
      readed: "",
      birthday: "",

      loading: false
    };
  },
  created() {
    this.$store.dispatch["tokenModule/checkToken"];
  },
  mounted() {
    if (!this.$store.getters["profileModule/checkUser"]) {
      this.loading = true;
      Api.get("/profile")
        .then(data => {
          this.$store.dispatch("profileModule/getProfileData", data.data);
        })
        .then(() => {
          const currentProfileState = this.$store.getters[
            "profileModule/getInfo"
          ];

          this.login = currentProfileState.login;
          this.favbooks = currentProfileState.favbooks;
          this.favgenre = currentProfileState.favgenre;
          this.wantRead = currentProfileState.wantread;
          this.readed = currentProfileState.readed;
          this.birthday = new Date(currentProfileState.birthday);
        })
        .catch(async () => {
          this.$store.dispatch("setError", "some problems with data,try again");
        })
        .finally(() => (this.loading = false));
    } else {
      const currentProfileState = this.$store.getters["profileModule/getInfo"];
      this.login = currentProfileState.login;
      this.favbooks = currentProfileState.favbooks;
      this.favgenre = currentProfileState.favgenre;
      this.wantRead = currentProfileState.wantread;
      this.readed = currentProfileState.readed;
      this.birthday = new Date(currentProfileState.birthday);
    }
  },
  computed: {
    ageHandler() {
      function calculate_age(birth_month, birth_day, birth_year) {
        const today_date = new Date();
        const today_year = today_date.getFullYear();
        const today_month = today_date.getMonth();
        const today_day = today_date.getDate();
        let age = today_year - birth_year;

        if (today_month < birth_month - 1) {
          age--;
        }
        if (birth_month - 1 == today_month && today_day < birth_day) {
          age--;
        }
        return age;
      }
      this.birthday = new Date(this.birthday);
      return calculate_age(
        this.birthday.getMonth(),
        this.birthday.getDate(),
        this.birthday.getFullYear()
      );
    }
  }
};
</script>

<style lang="scss" scoped>
.wrapper {
  min-width: 100%;
  position: absolute;
  top: 0;
  left: 0;
  margin-top: 100px;
}
.bookList__wrapper {
  display: flex;
  justify-content: center;
  text-align: center;
}

.card {
  width: 400px;
  border: none;
  border-radius: 10px;
  background-color: #fff;
}

.stats {
  background: #f2f5f8 !important;
  color: #000 !important;
}

.articles {
  font-size: 10px;
  color: #a1aab9;
}

.number1 {
  font-weight: 500;
}

.followers {
  font-size: 10px;
  color: #a1aab9;
}

.number2 {
  font-weight: 500;
}

.rating {
  font-size: 10px;
  color: #a1aab9;
}

.number3 {
  font-weight: 500;
}

@media screen and (max-width: 600px) {
  .bookList__wrapper {
    display: block;
    margin: auto;
  }
}
</style>
