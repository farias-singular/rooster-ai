```csharp
namespace Project.Tests.Domain.Brands
{
    public class BrandFactoryTest
    {
        private readonly IBrandUniquenessChecker _brandUniquenessChecker = Substitute.For<IBrandUniquenessChecker>();
        private readonly IBrandFactory _brandFactory;

        public BrandFactoryTest()
        {
            _brandFactory = new BrandFactory();
        }

        [Fact]
        public void CreateBrand_ValidData_ReturnsBrand()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();
            var id = "brand-id";
            var name = "brand-name";
            var title = "brand-title";

            _brandUniquenessChecker.IsUnique(id, organization.Id).Returns(true);

            // Act
            var brand = _brandFactory.Create(id, organization, category, name, title);

            // Assert
            Assert.NotNull(brand);
            Assert.Equal(id, brand.Id);
            Assert.Equal(organization.Id, brand.OrganizationId);
            Assert.Equal(category.Id, brand.CategoryId);
            Assert.Equal(name, brand.Name);
            Assert.Equal(title, brand.Title);
        }

        [Fact]
        public void CreateBrand_WithEmptyName_ThrowsException()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();
            var id = "brand-id";
            var name = "";
            var title = "brand-title";

            _brandUniquenessChecker.IsUnique(id, organization.Id).Returns(true);

            // Act & Assert
            var ex = Assert.Throws<BusinessRuleValidationException>(
                () => _brandFactory.Create(id, organization, category, name, title));

            Assert.Equal("Name must not be empty.", ex.Details);
        }

        [Fact]
        public void CreateBrand_WithEmptyTitle_ThrowsException()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();
            var id = "brand-id";
            var name = "brand-name";
            var title = "";

            _brandUniquenessChecker.IsUnique(id, organization.Id).Returns(true);

            // Act & Assert
            var ex = Assert.Throws<BusinessRuleValidationException>(
                () => _brandFactory.Create(id, organization, category, name, title));

            Assert.Equal("Title must not be empty.", ex.Details);
        }

        [Fact]
        public void CreateBrand_WithNullTitle_ReturnsBrand()
        {
            // Arrange
            var organization = EntityFaker.RandomOrganization();
            var category = EntityFaker.RandomCategory();
            var id = "brand-id";
            var name = "brand-name";
            string? title = null;

            _brandUniquenessChecker.IsUnique(id, organization.Id).Returns(true);

            // Act
            var brand = _brandFactory.Create(id, organization, category, name, title);

            // Assert
            Assert.NotNull(brand);
            Assert.Equal(id, brand.Id);
            Assert.Equal(organization.Id, brand.OrganizationId);
            Assert.Equal(category.Id, brand.CategoryId);
            Assert.Equal(name, brand.Name);
            Assert.Null(brand.Title);
        }
    }
}
```