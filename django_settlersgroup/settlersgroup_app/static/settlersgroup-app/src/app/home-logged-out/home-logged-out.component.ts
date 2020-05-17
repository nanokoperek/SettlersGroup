import { Component, OnInit, HostListener } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MaterialDialogComponent } from '../material-dialog/material-dialog.component';

@Component({
  selector: 'app-home-logged-out',
  templateUrl: './home-logged-out.component.html',
  styleUrls: ['./home-logged-out.component.scss']
})
export class HomeLoggedOutComponent implements OnInit {

  constructor(public dialog: MatDialog) {
  }

  ngOnInit(): void {
  }

  @HostListener('window:scroll', ['$event'])
  onWindowScroll(e) {
    const navbar = document.getElementById('sticky-nav');

    if (window.pageYOffset >= 170) {
      navbar.style.display = 'flex';
      navbar.classList.add('sticky');
    }
    else{
      navbar.classList.remove('sticky');
      navbar.style.display = 'none';
    }
  }

  public scrollToAboutUs(): void {
    document.getElementById('about-us').scrollIntoView();
  }

  public scrollToGallery(): void {
    document.getElementById('gallery').scrollIntoView();
  }

  public scrollToTop(): void {
    window.scrollTo(0, 0);
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(MaterialDialogComponent, {});
  }
}

