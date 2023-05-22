<script>
import { Editor, EditorContent } from '@tiptap/vue-3'
import StarterKit from '@tiptap/starter-kit'

export default {
  components: {
    EditorContent,
  },
  data() {
    return {
      editor: null,
    }
  },
  mounted() {
    this.editor = new Editor({
      extensions: [
        StarterKit,
      ],
      content: '',
    })
  },
  beforeUnmount() {
    this.editor.destroy()
  },
  methods: {
    submit() {
      const json = this.editor.getJSON()
      console.log(json)
    }
  },
}
</script>

<template>
  <div v-if="editor">
    <button @click="editor.chain().focus().toggleBold().run()" :class="{ 'is-active': editor.isActive('bold') }" class="main-feed-editor-button">
      B
    </button>
    <button @click="editor.chain().focus().toggleItalic().run()" :class="{ 'is-active': editor.isActive('italic') }" class="main-feed-editor-button">
      I
    </button>
    <button @click="editor.chain().focus().toggleStrike().run()" :class="{ 'is-active': editor.isActive('strike') }" class="main-feed-editor-button">
      S
    </button>
    <button @click="submit()" class="main-feed-send-button">Отправить</button>
  </div>
  <editor-content :editor="editor" class="main-feed-send-input" />
</template>

<style scoped>

.main-feed-send-input {
    width: 45rem;
    line-height: 3rem;
    border: 1px solid var(--white-color);
    border-radius: 5px;
    color: var(--white-color);
    resize: both;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
}
.main-feed-editor-button {
    border: 1px solid var(--white-color);
    border-radius: 5px;
    background: var(--black-color);
    color: var(--white-color);
    width: 3rem;
    height: 1rem;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
}
.main-feed-send-button {
    border: 1px solid var(--white-color);
    border-radius: 5px;
    background: var(--black-color);
    color: var(--white-color);
    width: 7rem;
    box-shadow: 0px 0px 20px var(--shadow-white-color), 0px 10px 20px var(--shadow-white-color);
}
</style>
