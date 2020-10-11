<template>
  <div class="googleLogin">
    <div class="intro_of_app">
      <v-card class="mx-auto my-12" max-width="374">
        <template slot="progress">
          <v-progress-linear
            color="deep-purple"
            height="10"
            indeterminate
          ></v-progress-linear>
        </template>

        <v-img height="250" :src="logo_img"></v-img>

        <v-card-title>Language Matching Web App</v-card-title>
        <v-card-text>
          <div>
            For english speakers, you can search and send likes to Japanese
            speakers who want to learn English. If the Japanese speaker also
            sends you a like, you can communicate with him/her in the chat room.
          </div>
        </v-card-text>
        <v-divider class="mx-4"></v-divider>
        <v-card-title>
          言語学習マッチングアプリ
        </v-card-title>
        <v-card-text>
          <div>
            日本語話者の方は、日本語を学びたい英語話者を探していいねを送ることができます。
            その英語話者もあなたにいいねを送ると、マッチングが成立してwebアプリ内でチャットすることができます。
          </div>
        </v-card-text>
      </v-card>
    </div>
    <div class="buttonLogin">
      <v-btn x-large @click="googleLogin"
        >Googleでログイン <br />または新規登録</v-btn
      >
    </div>
    <!-- <div>
      <nuxt-link :to="{ path: 'register' }">
        <v-btn>新規登録ページへ</v-btn>
      </nuxt-link>
    </div> -->
    <!-- <div class="buttonRegister">
      <nuxt-link to="/register">
        <v-btn>新規登録</v-btn>
      </nuxt-link>
    </div> -->
  </div>
</template>
<script>
import firebase from "@/plugins/firebase";
export default {
  data() {
    return {
      logo_img: "/images/pexels-mentatdgt-1346197-small.jpg"
    };
  },
  methods: {
    googleLogin() {
      const provider = new firebase.auth.GoogleAuthProvider();
      firebase.auth().signInWithRedirect(provider);
    }
  }
};
</script>
<style scoped>
.googleLogin {
  margin: 0 auto;
  text-align: center;
}

a {
  text-decoration: none;
}

.buttonLogin {
  margin: 20px;
}

.buttonRegisrer {
  margin: 20px;
}
</style>
