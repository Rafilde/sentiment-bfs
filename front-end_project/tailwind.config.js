/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors:{
        primary: 'var(--primary)',
        secondary: 'var(--secondary)',
        accent: 'var(--accent)',
        backgroundcolor: 'var(--backgroundcolor)',
        textcolor: 'var(--textcolor)',
      }
    },
  },
  plugins: [],
}

