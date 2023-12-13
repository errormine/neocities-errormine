const selectorHTML = `<aside id="theme-selector">
    <form action="">
        <fieldset>
            <legend>Website Theme</legend>
            <input type="radio" name="theme" id="light" checked>
            <label for="light">Light</label>
            <br>
            <input type="radio" name="theme" id="mason">
            <label for="mason">Mason</label>
            <br>
            <input type="radio" name="theme" id="dark">
            <label for="dark">Dark</label>
            <br>
            <input type="radio" name="theme" id="koyo">
            <label for="koyo">Koyo</label>
            <br>
            <input type="radio" name="theme" id="angel">
            <label for="angel">Angel</label>
        </fieldset>
    </form>
</aside>`;

document.querySelector("body").insertAdjacentHTML('beforebegin', selectorHTML);

const themeSelector = document.querySelector("#theme-selector");
const colorThemes = document.querySelectorAll('[name="theme"]');

themeSelector.classList.add("hidden");

const storeTheme = function(theme) {
    localStorage.setItem("theme", theme);
};

const setTheme = function() {
    const activeTheme = localStorage.getItem("theme");
    colorThemes.forEach((themeOption) => {
        if (themeOption.id == activeTheme) {
            themeOption.checked = true;
        }
    });
    document.documentElement.className = activeTheme;
};

colorThemes.forEach((themeOption) => {
    themeOption.addEventListener("click", () => {
        storeTheme(themeOption.id);
        setTheme();
    });
});

document.getElementsByTagName("h1")[0].addEventListener("click", () => {
    if (themeSelector.classList.contains("hidden"))
        themeSelector.classList.remove("hidden");
    else
        themeSelector.classList.add("hidden");
});

document.onload = setTheme();