8732936348087<!>/content/scripts/login.js<!>0<!>6931<!>0<!><!bool><!><div class="box_x_button box_x_tabs" onclick="curBox().hide()" aria-label="Закрыть" tabindex="0" role="button"></div>
<div class="login_user_name">Войти в другой аккаунт</div>
<div id="login_form_wrap" class="login_form_wrap login_box_form_wrap">
  <form method="post" name="login" id="login_form" action="vklogin">
    <input type="hidden" name="act" id="act" value="login">
    <input type="hidden" name="role" id="role" value="al_frame">
    <input type="hidden" name="expire" id="expire_input" value="" />
    <input type="hidden" name="_origin" value="https://vk.com" />
    <input type="hidden" name="ip_h" value="c4e380847ffc594daa" />
    <input type="hidden" name="lg_h" value="20d46f112dbaaae21a" />

    <input type="text" class="big_text" name="login" id="email" value="" placeholder="Телефон или email" />
    <input type="password" class="big_text" name="password" id="pass" value="" placeholder="Пароль" onkeyup="toggle('expire', !!this.value);toggle('login_forgot', !this.value);" />
    <div class="login_buttons_wrap">
      <button id="login_button" class="flat_button button_big_text login_button">Войти</button>
      <div class="login_forgot_wrap">
        <div class="checkbox" id="expire" onclick="checkbox(this);ge('expire_input').value=isChecked(this)?1:'';">Чужой компьютер</div>
        <a id="login_forgot" class="login_forgot" href="/restore">Забыли пароль?</a>
      </div>
    </div>
  </form>
</div><!>
addTemplates({"_":"_"});Login.init();<!><!json>[]