- {
  box-sizing: border-box;
  }

:root {
--background-color: hsl(0, 100%, 74%);
--color: hsl(257, 100%, 99%);
--font-size: 16px;
--font-size: 16px;
--font-family: sans-serif;
}

body {
background-color: var(--background-color);
color: var(--color);
font-family: var(--font-family);
font-size: var(--font-size);
background-image: url("./images/bg.png");
background-position: center;
background-attachment: fixed;
background-size: contain;
}

@media screen and (max-width: 600px) {
body {
/_ background-color: var(--background-color); _/
color: var(--color);
font-family: var(--font-family);
font-size: var(--font-size);
/_ background-color: rgb(7, 34, 5); _/
}
}

- {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  }

main {
width: 50%;
margin: auto;
display: flex;
justify-content: center;
/_ align-items: center; _/
height: 100vh;
flex-direction: column;
}

.top-text {
/_ background-color: moccasin; _/
padding: 2em;
font-size: 16px;
}
.top-text h1 {
color: white;
font-size: 30px;
padding-bottom: 10px;
font-size: bold;
}
/_ .top-text .top-p {
font-weight: bold;
font-size: 15px;
padding-bottom: 10px;
color: brown;
} _/
.whole-content {
display: flex;
width: 50%;
}

.whole-content .content1 {
padding: 2em;
width: 100%;
}

.content1 .p {
font-optical-sizing: auto;
font-family: "Lexend Deca script=latin rev=1";
font-weight: 300;
font-style: normal;
font-stretch: normal;
line-height: initial;
}
