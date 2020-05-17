import { Component, OnInit } from '@angular/core';
import { MatDialog } from '@angular/material/dialog';
import { MaterialDialogComponent } from '../material-dialog/material-dialog.component';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent implements OnInit {

  constructor(public dialog: MatDialog) { }

  ngOnInit(): void {
  }

  public scrollToAboutUs(): void {
    window.location.href = '#about-us';
  }

  public scrollToGallery(): void {
    window.location.href = '#gallery';
  }

  public scrollToTop(): void {
    window.scrollTo(0, 0);
  }

  openDialog(): void {
    const dialogRef = this.dialog.open(MaterialDialogComponent, {});
  }
}
