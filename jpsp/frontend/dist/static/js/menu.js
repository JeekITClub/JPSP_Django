/**
 * Created by ncj on 2017/8/20 2210.
 */
document.addEventListener('DOMContentLoaded', function () {

      // Get all "jpsp-menu-item" elements
      var $menuItems = Array.prototype.slice.call(document.querySelectorAll('.jpsp-menu-item'), 0)

      // Check if there are any menu items
      if ($menuItems.length > 0) {

        // Add a click event on each of them
        $menuItems.forEach(function ($el) {
          $el.addEventListener('click', function () {

            var $activeItem = document.querySelector('.is-active')
            // Toggle the class on the "jpsp-menu-item"
            if($activeItem != null) $activeItem.classList.toggle('is-active')
            $el.classList.toggle('is-active')

          })
        })
      }

    })
