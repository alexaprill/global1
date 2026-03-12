#!/usr/bin/env python3
"""
Transform 5 popup forms on the main page from single-step to two-step format.
Matches the pattern from the services page (rec1196707106 on page73305537.html).
"""

import re
import os
import shutil

FILE_PATH = '/Users/alexandra/Desktop/ZIP архив Tilda/site/global-generations/page62702763.html'
BACKUP_PATH = FILE_PATH + '.bak'

# Form definitions
FORMS = [
    {
        'rec_id': '977596041',
        'kto_lid': '7949696767510',
        'vozrast_lid': '7949696767511',
        'имя_lid': '7949696767512',
        'has_region': True,
        'region_lid': '1752179619441',
        'submit_text': 'Отправить',
        'service_tokens': None,  # keep existing
    },
    {
        'rec_id': '977608171',
        'kto_lid': '2899775960410',
        'vozrast_lid': '7299775960411',
        'имя_lid': '7299775960412',
        'has_region': False,
        'submit_text': 'Записаться на встречу',
        'service_tokens': None,
    },
    {
        'rec_id': '977606796',
        'kto_lid': '3069775960410',
        'vozrast_lid': '3079775960411',
        'имя_lid': '3079775960412',
        'has_region': False,
        'submit_text': 'Отправить',
        'service_tokens': None,
    },
    {
        'rec_id': '977607031',
        'kto_lid': '6629776067960',
        'vozrast_lid': '6629776067961',
        'имя_lid': '6629776067962',
        'has_region': False,
        'submit_text': 'Отправить',
        'service_tokens': None,
    },
    {
        'rec_id': '1196707106',
        'kto_lid': '2111966990610',
        'vozrast_lid': '4211966990611',
        'имя_lid': '7211966990612',
        'has_region': False,
        'submit_text': 'Отправить',
        'service_tokens': None,
    },
]


def build_screen1_html(rec_id):
    """Build the Screen 1 questionnaire HTML for a given form."""
    return f'''<div class="gg-screen" id="gg-screen1-{rec_id}">
<div class="t-form__inputsbox t-form__inputsbox_vertical-form t-form__inputsbox_inrow">

<div class="gg-q-title">Я...</div>
<div class="gg-radio-group">
<label class="gg-radio-item"><input type="radio" name="Кто" value="Я — родитель" onchange="var a=document.getElementById('gg-age-row-{rec_id}');if(a)a.classList.remove('gg-show');"><span>Я — родитель</span></label>
<label class="gg-radio-item"><input type="radio" name="Кто" value="Я — ученик" onchange="var a=document.getElementById('gg-age-row-{rec_id}');if(a)a.classList.add('gg-show');"><span>Я — ученик</span></label>
</div>
<div class="gg-age-row" id="gg-age-row-{rec_id}"><input type="text" name="Возраст" placeholder="Сколько вам лет?"></div>

<div class="gg-q-title">Сколько у вас времени на подготовку?</div>
<div class="gg-radio-group">
<label class="gg-radio-item"><input type="radio" name="Время на подготовку" value="0–6 месяцев"><span>0–6 месяцев</span></label>
<label class="gg-radio-item"><input type="radio" name="Время на подготовку" value="Полгода — год"><span>Полгода — год</span></label>
<label class="gg-radio-item"><input type="radio" name="Время на подготовку" value="Год — два"><span>Год — два</span></label>
<label class="gg-radio-item"><input type="radio" name="Время на подготовку" value="Больше двух лет"><span>Больше двух лет</span></label>
</div>

<div class="gg-q-title">Оцените уровень своей заявки/подготовки</div>
<div class="gg-radio-group">
<label class="gg-radio-item"><input type="radio" name="Уровень подготовки" value="Всё готово, необходима проверка"><span>Всё готово, необходима проверка</span></label>
<label class="gg-radio-item"><input type="radio" name="Уровень подготовки" value="Почти готово, нужна помощь с отдельными аспектами"><span>Почти готово, нужна помощь с отдельными аспектами</span></label>
<label class="gg-radio-item"><input type="radio" name="Уровень подготовки" value="Есть база: язык, оценки, активности"><span>Есть база: язык, оценки, активности</span></label>
<label class="gg-radio-item"><input type="radio" name="Уровень подготовки" value="Ничего нет"><span>Ничего нет</span></label>
</div>

<div class="gg-q-title">Бюджет</div>
<div class="gg-radio-group">
<label class="gg-radio-item"><input type="radio" name="Бюджет" value="До 5 000 $"><span>До 5 000 $</span></label>
<label class="gg-radio-item"><input type="radio" name="Бюджет" value="До 10 000 $"><span>До 10 000 $</span></label>
<label class="gg-radio-item"><input type="radio" name="Бюджет" value="До 15 000 $"><span>До 15 000 $</span></label>
<label class="gg-radio-item"><input type="radio" name="Бюджет" value="20 000 $ и более"><span>20 000 $ и более</span></label>
</div>

<div class="gg-q-title">Готовы ли вы рассмотреть наши услуги, чтобы повысить шанс на финансирование?</div>
<div class="gg-radio-group">
<label class="gg-radio-item"><input type="radio" name="Готовность" value="Да, хочу начать сейчас"><span>Да, хочу начать сейчас</span></label>
<label class="gg-radio-item"><input type="radio" name="Готовность" value="Решу после консультации"><span>Решу после консультации</span></label>
<label class="gg-radio-item"><input type="radio" name="Готовность" value="Возможно в будущем"><span>Возможно в будущем</span></label>
<label class="gg-radio-item"><input type="radio" name="Готовность" value="Нет, только бесплатные материалы"><span>Нет, только бесплатные материалы</span></label>
</div>

<div class="gg-error-msg" id="gg-error-msg-{rec_id}">Пожалуйста, ответьте на все вопросы</div>
<script>
function ggValidateAndNext_{rec_id}(){{
  var names=['Кто','Время на подготовку','Уровень подготовки','Бюджет','Готовность'];
  for(var i=0;i<names.length;i++){{
    var sel=document.querySelector('#gg-screen1-{rec_id} input[name="'+names[i]+'"]:checked');
    if(!sel){{document.getElementById('gg-error-msg-{rec_id}').style.display='block';return;}}
  }}
  document.getElementById('gg-error-msg-{rec_id}').style.display='none';
  document.getElementById('gg-screen1-{rec_id}').classList.add('gg-hidden');
  document.getElementById('gg-screen2-{rec_id}').classList.remove('gg-hidden');
  document.getElementById('popuptitle_{rec_id}').textContent='Где с вами связаться?';
  document.getElementById('rec{rec_id}').classList.add('gg-screen2-active');
}}
</script>
<button type="button" class="gg-btn" onclick="ggValidateAndNext_{rec_id}();">Продолжить</button>
</div></div><!-- end screen 1 -->'''


def build_screen2_open(rec_id):
    """Build Screen 2 opening HTML with back button."""
    return f'''
<div class="gg-screen gg-hidden" id="gg-screen2-{rec_id}">
<div style="margin-bottom:12px;"><button type="button" style="background:none;border:none;color:#182849;cursor:pointer;font-size:13px;padding:0;opacity:0.6;" onclick="document.getElementById('gg-screen2-{rec_id}').classList.add('gg-hidden');document.getElementById('gg-screen1-{rec_id}').classList.remove('gg-hidden');document.getElementById('popuptitle_{rec_id}').textContent='Расскажите о себе';document.getElementById('rec{rec_id}').classList.remove('gg-screen2-active');">&larr; Назад</button></div>
<div class="t-form__inputsbox t-form__inputsbox_vertical-form t-form__inputsbox_inrow">'''


def build_css_block(rec_id):
    """Build the CSS block for gg-* classes scoped to a rec ID."""
    return f'''<style>
#rec{rec_id} .gg-screen{{transition:opacity 0.3s ease,max-height 0.3s ease;}}
#rec{rec_id} .gg-screen.gg-hidden{{opacity:0;max-height:0;overflow:hidden;pointer-events:none;position:absolute;}}
#rec{rec_id} .gg-q-title{{font-family:'Mulish',Arial,sans-serif;font-size:14px;font-weight:700;color:#182849;margin:20px 0 10px 0;}}
#rec{rec_id} .gg-q-title:first-child{{margin-top:0;}}
#rec{rec_id} .gg-radio-group{{list-style:none;margin:0;padding:0;}}
#rec{rec_id} .gg-radio-item{{display:flex;align-items:center;margin-bottom:10px;cursor:pointer;font-family:'Mulish',Arial,sans-serif;font-size:14px;color:#182849;}}
#rec{rec_id} .gg-radio-item input[type="radio"]{{-webkit-appearance:none;-moz-appearance:none;appearance:none;width:22px;height:22px;min-width:22px;border:2px solid #b0b8c9;border-radius:50%;margin:0 12px 0 0;cursor:pointer;position:relative;transition:border-color .2s;}}
#rec{rec_id} .gg-radio-item input[type="radio"]:checked{{border-color:#182849;}}
#rec{rec_id} .gg-radio-item input[type="radio"]:checked::after{{content:'';position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);width:12px;height:12px;background:#182849;border-radius:50%;}}
#rec{rec_id} .gg-radio-item:hover input[type="radio"]{{border-color:#182849;}}
#rec{rec_id} .gg-btn{{display:block;width:100%;padding:16px;border:none;border-radius:30px;background:#182849;color:#fff;font-family:'Mulish',Arial,sans-serif;font-size:16px;font-weight:700;cursor:pointer;margin-top:24px;transition:background .2s;text-transform:uppercase;letter-spacing:0.5px;}}
#rec{rec_id} .gg-btn:hover{{background:#00C1DE;}}
#rec{rec_id} .gg-age-row{{margin:8px 0 0 34px;display:none;}}
#rec{rec_id} .gg-age-row.gg-show{{display:block;}}
#rec{rec_id} .gg-age-row input{{width:100%;padding:10px 14px;border:1px solid #182849;border-radius:5px;font-family:'Mulish',Arial,sans-serif;font-size:14px;color:#182849;box-sizing:border-box;}}
#rec{rec_id} .gg-error-msg{{color:#ff4444;font-family:'Mulish',Arial,sans-serif;font-size:12px;margin-top:8px;display:none;}}
#rec{rec_id} .t-submit .t-btnflex__text{{text-transform:uppercase;font-weight:700;letter-spacing:0.5px;}}
#rec{rec_id} .t-btnflex.t-btnflex_type_submit{{border-radius:30px !important;}}
#rec{rec_id} .t702__form-bottom-text{{display:none;}}
#rec{rec_id}.gg-screen2-active .t702__form-bottom-text{{display:block;}}
</style>'''


def transform_form(html, form_def):
    """Transform a single form from single-step to two-step."""
    rec_id = form_def['rec_id']
    kto_lid = form_def['kto_lid']
    vozrast_lid = form_def['vozrast_lid']
    имя_lid = form_def['имя_lid']
    has_region = form_def['has_region']

    print(f"\n--- Processing rec{rec_id} ---")

    # Step 1: Change the popup title from static to "Расскажите о себе"
    # Find: <div class="t702__title t-title t-title_xxs" id="popuptitle_{rec_id}">...</div>
    title_pattern = (
        r'(<div\s+class="t702__title\s+t-title\s+t-title_xxs"\s+id="popuptitle_'
        + re.escape(rec_id)
        + r'">)'
        + r'(.*?)'
        + r'(</div>)'
    )
    title_match = re.search(title_pattern, html, re.DOTALL)
    if title_match:
        old_title = title_match.group(0)
        new_title = title_match.group(1) + 'Расскажите о себе' + title_match.group(3)
        html = html.replace(old_title, new_title, 1)
        print(f"  Title changed from '{title_match.group(2).strip()}' to 'Расскажите о себе'")
    else:
        print(f"  WARNING: Title not found for rec{rec_id}")

    # Step 2: Find the successbox end marker, then inject CSS + Screen1 before inputsbox,
    # and restructure fields into Screen 2.
    #
    # Strategy: We need to find and replace the content inside the form.
    # The structure is:
    #   <div class="js-successbox ...">...</div>
    #   <div class="t-form__inputsbox ...">
    #     [Кто radio group]
    #     [Возраст field]
    #     [Region field - only form 1]
    #     [Имя field]
    #     [Email field]
    #     [Phone field]
    #     [Способ связи]
    #     [ник field]
    #     [промокод checkbox]
    #     [Промокод input]
    #     [conditional script]
    #     <div class="t-form__errorbox-middle">...
    #     <div class="t-form__submit">...
    #   </div> (inputsbox close)
    #   <div class="t-form__errorbox-bottom">...
    #
    # We need to:
    # a) Remove the Кто, Возраст, Region fields
    # b) Insert CSS + Screen1 before the Имя field
    # c) Wrap Имя through Промокод + errorbox-middle + submit in Screen2
    # d) Close Screen2 after errorbox-bottom

    # Find the inputsbox opening for this form. We'll use the successbox as an anchor.
    # The successbox ends, then the inputsbox starts.

    # Let's find the section between successbox end and the Имя field.
    # We need to locate:
    # 1. The end of successbox: style="display:none;"></div> <div\nclass="t-form__inputsbox
    # 2. The Кто radio div start: data-input-lid="{kto_lid}"
    # 3. The Имя field start: data-input-lid="{имя_lid}"

    # Find the inputsbox opening right before the Кто field for this form
    # We search for the inputsbox opening that is followed (eventually) by the kto_lid

    # Let's find the Кто field start marker
    kto_marker = f'data-input-lid="{kto_lid}"'
    kto_pos = html.find(kto_marker)
    if kto_pos == -1:
        print(f"  ERROR: Кто field (lid={kto_lid}) not found!")
        return html

    # Find the div start before the kto_marker (the t-input-group div)
    # Search backwards from kto_pos for '<div'
    kto_div_start = html.rfind('<div', 0, kto_pos)
    # Verify it's a t-input-group
    kto_div_snippet = html[kto_div_start:kto_pos+50]
    print(f"  Found Кто div at pos {kto_div_start}")

    # Find the Имя field start
    имя_marker = f'data-input-lid="{имя_lid}"'
    имя_pos = html.find(имя_marker, kto_pos)
    if имя_pos == -1:
        print(f"  ERROR: Имя field (lid={имя_lid}) not found!")
        return html

    # Find the div start before the Имя marker
    имя_div_start = html.rfind('<div', 0, имя_pos)
    print(f"  Found Имя div at pos {имя_div_start}")

    # Now find the inputsbox opening before the Кто field
    # Search backwards from kto_div_start for 't-form__inputsbox'
    inputsbox_marker = 't-form__inputsbox'
    inputsbox_search_area = html[max(0, kto_div_start-500):kto_div_start]
    inputsbox_rel_pos = inputsbox_search_area.rfind(inputsbox_marker)
    if inputsbox_rel_pos == -1:
        print(f"  ERROR: inputsbox not found before Кто field!")
        return html

    # Find the actual '<div' that starts the inputsbox
    inputsbox_area_start = max(0, kto_div_start - 500)
    inputsbox_div_start = inputsbox_search_area.rfind('<div', 0, inputsbox_rel_pos)
    inputsbox_abs_start = inputsbox_area_start + inputsbox_div_start

    # Find the '>' that closes the inputsbox opening tag
    inputsbox_tag_end = html.find('>', inputsbox_abs_start) + 1
    print(f"  Found inputsbox opening tag: pos {inputsbox_abs_start} to {inputsbox_tag_end}")

    # The section to remove: from kto_div_start to имя_div_start
    # This includes: Кто radio group, Возраст field, (Region field for form 1)
    remove_section = html[kto_div_start:имя_div_start]
    print(f"  Section to remove between Кто and Имя: {len(remove_section)} chars")

    # Verify the section contains what we expect
    if kto_marker not in remove_section:
        print(f"  ERROR: Remove section doesn't contain Кто marker!")
        return html
    if f'data-input-lid="{vozrast_lid}"' not in remove_section:
        print(f"  ERROR: Remove section doesn't contain Возраст marker!")
        return html
    if has_region:
        region_lid = form_def['region_lid']
        if f'data-input-lid="{region_lid}"' not in remove_section:
            print(f"  ERROR: Remove section doesn't contain Region marker!")
            return html
        print(f"  Region field found in remove section (lid={region_lid})")

    # Now we need to find the errorbox-middle and submit sections to wrap in Screen 2.
    # The conditional script + errorbox-middle comes after the Промокод field.
    # We need to find the closing of the inputsbox div and the errorbox-bottom closing.

    # Find errorbox-middle for this form (after Имя field)
    errorbox_middle_marker = '<div class="t-form__errorbox-middle">'
    # There may be multiple errorbox-middle in the file, find the right one
    errorbox_middle_pos = html.find(errorbox_middle_marker, имя_pos)
    if errorbox_middle_pos == -1:
        print(f"  ERROR: errorbox-middle not found after Имя field!")
        return html

    # Verify this errorbox is for our form by checking it's before the next form's rec div
    # Find the </form> after our form
    form_end_marker = f'</form>'
    form_end_pos = html.find(form_end_marker, имя_pos)
    if errorbox_middle_pos > form_end_pos:
        print(f"  ERROR: errorbox-middle found after form end!")
        return html

    print(f"  Found errorbox-middle at pos {errorbox_middle_pos}")

    # Find the errorbox-bottom closing for this form
    errorbox_bottom_marker = '<div class="t-form__errorbox-bottom">'
    errorbox_bottom_pos = html.find(errorbox_bottom_marker, errorbox_middle_pos)
    if errorbox_bottom_pos == -1 or errorbox_bottom_pos > form_end_pos:
        print(f"  ERROR: errorbox-bottom not found!")
        return html

    # Find the end of errorbox-bottom (it closes with </div> <!--/noindex--> </div>)
    # The structure after errorbox-bottom is:
    # <div class="t-form__errorbox-bottom"> <!--noindex--> <div ...> <ul ...>...</ul> </div> <!--/noindex--> </div>
    # Then </form>
    # We need to find the closing </div> of errorbox-bottom
    # Let's find the <!--/noindex--> </div> pattern after errorbox-bottom
    noindex_end = html.find('<!--/noindex--> </div>', errorbox_bottom_pos)
    if noindex_end == -1:
        print(f"  ERROR: noindex end not found after errorbox-bottom!")
        return html
    errorbox_bottom_end = noindex_end + len('<!--/noindex--> </div>')
    print(f"  Found errorbox-bottom end at pos {errorbox_bottom_end}")

    # Now find the conditional form script that appears between Промокод and errorbox-middle.
    # This script contains t_form__conditionals_initFields and is between the last field and errorbox-middle.
    # It's already included in the section between имя_div_start and errorbox-middle_pos, so it'll
    # naturally be inside Screen 2.

    # Now construct the replacement.
    #
    # Original structure (simplified):
    #   [inputsbox open tag]
    #     [Кто field]
    #     [Возраст field]
    #     [Region field - form 1 only]
    #     [Имя field]
    #     ...
    #     [Промокод field]
    #     [conditional script]
    #     [errorbox-middle]
    #     [submit button]
    #   [inputsbox close - implicit </div>]
    #   [errorbox-bottom]
    #
    # New structure:
    #   [CSS block]
    #   [Screen 1 div with questionnaire + inputsbox inside]
    #   [Screen 2 opening + back button]
    #   [inputsbox open tag]  <-- new inputsbox for screen 2
    #     [Имя field]
    #     ...
    #     [Промокод field]
    #     [conditional script]
    #     [errorbox-middle]
    #     [submit button]
    #   [inputsbox close]
    #   [errorbox-bottom]
    #   </div><!-- end screen 2 -->

    # The approach:
    # 1. Replace from inputsbox_tag_end through имя_div_start with:
    #    close inputsbox </div> + CSS + Screen1 + Screen2 open + new inputsbox open
    # Wait, that's not right. Let me reconsider.

    # Actually, looking at the reference more carefully:
    # The reference has TWO inputsbox divs - one inside Screen 1, one inside Screen 2.
    # Screen 1 has its own inputsbox with the questionnaire.
    # Screen 2 has its own inputsbox with the contact fields.
    # Both screens are inside the form, outside any inputsbox.

    # So the transformation should be:
    # Replace the original single inputsbox with:
    #   CSS + Screen1(with its own inputsbox) + Screen2(with its own inputsbox + errorboxes + submit)
    #
    # The original </div> that closes the inputsbox is somewhere. Let's find it.
    # Actually, the errorbox-middle and submit are INSIDE the inputsbox div (based on the original HTML).
    # Looking at the original: the inputsbox contains all fields + the conditional script,
    # then errorbox-middle and submit are siblings after inputsbox close? No...

    # Let me re-examine the original structure more carefully.
    # From the read output (form 1):
    # Line 2120-2122: <div class="t-form__inputsbox ...">
    # Line 2123: [Кто field starts]
    # ...
    # Line 2283: [conditional script + t-form__screen-hiderecord]
    # Line 2283: <div class="t-form__errorbox-middle">
    # Line 2289: <div class="t-form__submit">
    # Line 2291: </div> (close of something)
    # Line 2291: <div class="t-form__errorbox-bottom">
    # ...
    # Then </form>

    # And from the reference (services page):
    # Line 1653: style="display:none;"></div>
    # Line 1654: <style> (CSS block)
    # Line 1676: <div class="gg-screen" id="gg-screen1">
    # Line 1677: <div class="t-form__inputsbox ..."> (Screen 1's inputsbox)
    # ...
    # Line 1734: </div></div><!-- end screen 1 -->
    # Line 1736: <div class="gg-screen gg-hidden" id="gg-screen2">
    # Line 1737: [back button]
    # Line 1738: <div class="t-form__inputsbox ..."> (Screen 2's inputsbox)
    # ...fields...
    # Line 1825: [conditional script]
    # Line 1825: <div class="t-form__errorbox-middle">
    # Line 1831: <div class="t-form__submit">
    # ...
    # Line 1833: </div> (close of something - probably the inner wrapper)
    # Line 1833: <div class="t-form__errorbox-bottom">
    # ...
    # Line 1840: </div><!-- end screen 2 -->
    # Line 1841: </form>

    # So in the reference: errorbox-middle, submit, and errorbox-bottom are ALL inside Screen 2.
    # The </div> that closes the inputsbox in Screen 2 is implicit - it's part of the </div> chain.

    # Let me trace the div nesting in the reference:
    # Screen2 div opens
    #   back button div
    #   inputsbox div opens (Screen 2's)
    #     [fields]
    #     errorbox-middle div
    #     submit div
    #   inputsbox div closes (the </div> after submit's </div>)
    #   errorbox-bottom div
    # screen2 div closes (</div><!-- end screen 2 -->)

    # Wait, looking at line 1833 from reference:
    # ...submit button...</button> </div> </div> <div class="t-form__errorbox-bottom">
    # Those two </div>s close the submit div and then... one more level.

    # Actually on the original main page, the structure after the inputsbox opening is:
    # inputsbox opens
    #   [fields...]
    #   [conditional script block]
    #   errorbox-middle { ... }
    #   submit { ... }
    # inputsbox closes </div>
    # errorbox-bottom { ... }
    # </form>

    # So errorbox-middle and submit are INSIDE inputsbox, errorbox-bottom is OUTSIDE inputsbox.

    # In the reference:
    # screen2 opens
    #   back button
    #   inputsbox opens (screen 2)
    #     [fields]
    #     [conditional script]
    #     errorbox-middle
    #     submit
    #   inputsbox closes
    #   errorbox-bottom
    # screen2 closes

    # So errorbox-bottom is inside screen2 but outside inputsbox. That matches.
    # The screen2 close div is AFTER errorbox-bottom.

    # Now let me plan the surgery:
    #
    # ORIGINAL (from inputsbox_abs_start to errorbox_bottom_end):
    #   <div class="t-form__inputsbox ...">      <-- inputsbox open
    #     [Кто field]
    #     [Возраст field]
    #     [Region - form1 only]
    #     [Имя field]
    #     ...all other fields...
    #     [conditional script]
    #     [errorbox-middle]
    #     [submit]
    #   </div>                                     <-- inputsbox close
    #   [errorbox-bottom]
    #
    # REPLACEMENT:
    #   [CSS block]
    #   <div class="gg-screen" id="gg-screen1-{id}">
    #     <div class="t-form__inputsbox ...">      <-- screen1 inputsbox
    #       [questionnaire HTML]
    #     </div>
    #   </div><!-- end screen 1 -->
    #   <div class="gg-screen gg-hidden" id="gg-screen2-{id}">
    #     [back button]
    #     <div class="t-form__inputsbox ...">      <-- screen2 inputsbox
    #       [Имя field through Промокод field]
    #       [conditional script]
    #       [errorbox-middle]
    #       [submit]
    #     </div>                                    <-- screen2 inputsbox close
    #     [errorbox-bottom]
    #   </div><!-- end screen 2 -->

    # But wait - I need to find where the inputsbox closing </div> is.
    # The inputsbox opening is at inputsbox_abs_start.
    # The submit button div ends with </div>, and then there should be the closing </div> for inputsbox.
    # Let me find it by looking at what's between submit end and errorbox-bottom.

    # Actually, let me look at the original HTML more carefully from the read output.
    # Line 2289 (form 1):
    # <div class="t-form__submit"> <button ...>...</button> </div>
    # Then immediately:
    # </div>   <-- this closes the inputsbox
    # <div class="t-form__errorbox-bottom">

    # But looking at the actual text on line 2291:
    # type="submit"><span class="t-btnflex__text">Отправить</span> <style>...</style></button> </div> </div> <div class="t-form__errorbox-bottom">
    # So: </button> </div> </div> <div class="t-form__errorbox-bottom">
    # The first </div> closes the submit div, the second </div> closes the inputsbox.

    # So between submit button end and errorbox-bottom there are TWO </div>s.
    # I need to keep both in the replacement and add the screen2 wrapping.

    # Actually, simpler approach: I'll replace the entire section from the inputsbox opening
    # through errorbox-bottom end with the new two-screen structure.

    # Let me extract the pieces I need to keep:
    # 1. The Имя through Промокод fields + conditional script
    # 2. The errorbox-middle
    # 3. The submit button
    # 4. The inputsbox close
    # 5. The errorbox-bottom

    # Extract the kept fields section: from имя_div_start to errorbox_middle_pos
    kept_fields = html[имя_div_start:errorbox_middle_pos]

    # Extract from errorbox_middle through errorbox_bottom_end
    errorbox_and_submit = html[errorbox_middle_pos:errorbox_bottom_end]

    # Now build the full replacement
    css_block = build_css_block(rec_id)
    screen1_html = build_screen1_html(rec_id)
    screen2_open = build_screen2_open(rec_id)

    # The replacement for the entire section from inputsbox_abs_start to errorbox_bottom_end
    replacement = (
        css_block + '\n'
        + screen1_html + '\n'
        + screen2_open + ' '
        + kept_fields
        + errorbox_and_submit
        + '\n</div><!-- end screen 2 -->'
    )

    # Do the replacement
    original_section = html[inputsbox_abs_start:errorbox_bottom_end]
    html = html[:inputsbox_abs_start] + replacement + html[errorbox_bottom_end:]

    print(f"  Replaced {len(original_section)} chars with {len(replacement)} chars")
    print(f"  Form rec{rec_id} transformation complete!")

    return html


def verify_transformation(html, form_def):
    """Verify that a form was correctly transformed."""
    rec_id = form_def['rec_id']
    checks = []

    # Check Screen 1 exists
    if f'id="gg-screen1-{rec_id}"' in html:
        checks.append(f"  [OK] Screen 1 div found (gg-screen1-{rec_id})")
    else:
        checks.append(f"  [FAIL] Screen 1 div NOT found (gg-screen1-{rec_id})")

    # Check Screen 2 exists
    if f'id="gg-screen2-{rec_id}"' in html:
        checks.append(f"  [OK] Screen 2 div found (gg-screen2-{rec_id})")
    else:
        checks.append(f"  [FAIL] Screen 2 div NOT found (gg-screen2-{rec_id})")

    # Check title was changed
    if f'id="popuptitle_{rec_id}">Расскажите о себе</div>' in html:
        checks.append(f"  [OK] Title changed to 'Расскажите о себе'")
    else:
        checks.append(f"  [FAIL] Title NOT changed")

    # Check CSS block exists
    if f'#rec{rec_id} .gg-screen{{' in html or f'#rec{rec_id} .gg-screen{{transition' in html:
        checks.append(f"  [OK] CSS block found")
    else:
        checks.append(f"  [FAIL] CSS block NOT found")

    # Check validation function exists
    if f'function ggValidateAndNext_{rec_id}()' in html:
        checks.append(f"  [OK] Validation function found")
    else:
        checks.append(f"  [FAIL] Validation function NOT found")

    # Check back button exists
    if f"gg-screen1-{rec_id}').classList.remove('gg-hidden')" in html:
        checks.append(f"  [OK] Back button found")
    else:
        checks.append(f"  [FAIL] Back button NOT found")

    # Check Кто radio is now custom (not Tilda native)
    kto_lid = form_def['kto_lid']
    if f'data-input-lid="{kto_lid}"' not in html:
        checks.append(f"  [OK] Tilda native Кто field removed (lid={kto_lid})")
    else:
        checks.append(f"  [FAIL] Tilda native Кто field still present (lid={kto_lid})")

    # Check Возраст native field removed
    vozrast_lid = form_def['vozrast_lid']
    if f'data-input-lid="{vozrast_lid}"' not in html:
        checks.append(f"  [OK] Tilda native Возраст field removed (lid={vozrast_lid})")
    else:
        checks.append(f"  [FAIL] Tilda native Возраст field still present (lid={vozrast_lid})")

    # Check Region removed (form 1 only)
    if form_def['has_region']:
        region_lid = form_def['region_lid']
        if f'data-input-lid="{region_lid}"' not in html:
            checks.append(f"  [OK] Region field removed (lid={region_lid})")
        else:
            checks.append(f"  [FAIL] Region field still present (lid={region_lid})")

    # Check Имя field preserved
    имя_lid = form_def['имя_lid']
    if f'data-input-lid="{имя_lid}"' in html:
        checks.append(f"  [OK] Имя field preserved (lid={имя_lid})")
    else:
        checks.append(f"  [FAIL] Имя field NOT preserved (lid={имя_lid})")

    # Check questionnaire questions present
    for q in ['Время на подготовку', 'Уровень подготовки', 'Бюджет', 'Готовность']:
        # Check inside the screen1 for this form
        screen1_marker = f'id="gg-screen1-{rec_id}"'
        screen1_pos = html.find(screen1_marker)
        if screen1_pos != -1:
            # Check for the question in the vicinity
            screen1_end = html.find('<!-- end screen 1 -->', screen1_pos)
            screen1_section = html[screen1_pos:screen1_end] if screen1_end != -1 else ''
            if f'name="{q}"' in screen1_section:
                checks.append(f"  [OK] Question '{q}' found in Screen 1")
            else:
                checks.append(f"  [FAIL] Question '{q}' NOT found in Screen 1")

    # Check end screen 2 comment
    if f'</div><!-- end screen 2 -->' in html:
        checks.append(f"  [OK] Screen 2 closing comment found")
    else:
        checks.append(f"  [FAIL] Screen 2 closing comment NOT found")

    print(f"\nVerification for rec{rec_id}:")
    for c in checks:
        print(c)

    failures = [c for c in checks if '[FAIL]' in c]
    return len(failures) == 0


def main():
    print(f"Reading file: {FILE_PATH}")
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        html = f.read()

    print(f"File size: {len(html)} bytes, {html.count(chr(10))} lines")

    # Create backup
    shutil.copy2(FILE_PATH, BACKUP_PATH)
    print(f"Backup created: {BACKUP_PATH}")

    # Process each form
    for form_def in FORMS:
        html = transform_form(html, form_def)

    # Write the result
    with open(FILE_PATH, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"\nFile written: {FILE_PATH}")
    print(f"New file size: {len(html)} bytes")

    # Verify all transformations
    print("\n" + "="*60)
    print("VERIFICATION")
    print("="*60)

    all_ok = True
    for form_def in FORMS:
        if not verify_transformation(html, form_def):
            all_ok = False

    if all_ok:
        print("\n>>> ALL FORMS TRANSFORMED SUCCESSFULLY <<<")
    else:
        print("\n>>> SOME CHECKS FAILED - REVIEW OUTPUT <<<")


if __name__ == '__main__':
    main()
